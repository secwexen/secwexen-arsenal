"""Collect publicly available email addresses from a specified domain."""

import re
import socket
import sys
from typing import Set, List
from urllib.parse import urljoin

import requests

from utils import log_info, log_warning, is_valid_email


EMAIL_REGEX = re.compile(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
)

DEFAULT_PATHS = [
    "/",
    "/contact",
    "/about",
    "/team",
    "/staff",
    "/support",
    "/help",
]


def _normalize_domain(domain: str) -> str:
    """Remove a URL scheme and trailing slashes from a domain."""
    normalized_domain = domain.strip()

    if normalized_domain.startswith(("http://", "https://")):
        normalized_domain = normalized_domain.split("://", 1)[1]

    return normalized_domain.rstrip("/")


def _build_urls(domain: str, paths: List[str]) -> List[str]:
    """Build HTTP and HTTPS URLs for the specified paths."""
    urls = []

    for scheme in ("https://", "http://"):
        base_url = f"{scheme}{domain}"

        for path in paths:
            urls.append(urljoin(base_url, path))

    return urls


def _fetch_url(url: str, timeout: int = 10) -> str | None:
    """Fetch a URL and return its response body on a successful request."""
    try:
        response = requests.get(
            url,
            timeout=timeout,
            verify=True,
            allow_redirects=True,
        )

        if 200 <= response.status_code < 400:
            return response.text

        log_warning(
            f"[OSINT] Non-success status for {url}: "
            f"{response.status_code}"
        )

    except requests.RequestException as exc:
        log_warning(f"[OSINT] Failed to fetch {url}: {exc}")

    return None


def _extract_emails_from_text(text: str) -> Set[str]:
    """Extract and validate email addresses from text."""
    extracted_emails = set(EMAIL_REGEX.findall(text or ""))

    cleaned_emails = {
        email.strip().strip(".,;:")
        for email in extracted_emails
    }

    return {
        email
        for email in cleaned_emails
        if is_valid_email(email)
    }


def _filter_domain_emails(
    emails: Set[str],
    domain: str,
) -> Set[str]:
    """Keep only email addresses belonging to the specified domain."""
    normalized_domain = _normalize_domain(domain).lower()

    return {
        email
        for email in emails
        if email.lower().endswith("@" + normalized_domain)
    }


def _resolve_domain(domain: str) -> str | None:
    """Resolve a domain to an IPv4 address."""
    try:
        ip_address = socket.gethostbyname(domain)
        log_info(f"[OSINT] Resolved {domain} to {ip_address}")
        return ip_address

    except socket.gaierror:
        log_warning(f"[OSINT] Could not resolve domain: {domain}")
        return None


def harvest_emails(
    domain: str,
    only_domain: bool = True,
) -> Set[str]:
    """Collect email addresses from common public pages of a domain."""
    normalized_domain = _normalize_domain(domain)

    log_info(
        f"[OSINT] Starting email harvest for: {normalized_domain}"
    )

    _resolve_domain(normalized_domain)

    urls = _build_urls(normalized_domain, DEFAULT_PATHS)
    all_emails: Set[str] = set()

    for url in urls:
        log_info(f"[OSINT] Fetching: {url}")

        html = _fetch_url(url)
        if not html:
            continue

        page_emails = _extract_emails_from_text(html)

        if page_emails:
            log_info(
                f"[OSINT] Found {len(page_emails)} email(s) on {url}"
            )
            all_emails.update(page_emails)

    if only_domain:
        all_emails = _filter_domain_emails(
            all_emails,
            normalized_domain,
        )

    if not all_emails:
        log_warning(
            f"[OSINT] No emails found for domain: {normalized_domain}"
        )
    else:
        log_info(
            "[OSINT] Harvest completed. "
            f"Total unique emails: {len(all_emails)}"
        )

    return all_emails


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python email_harvester.py <domain>")
        sys.exit(1)

    target_domain = sys.argv[1]
    harvested_emails = harvest_emails(target_domain)

    print(f"\n[OSINT] Emails found for {target_domain}:")

    for email in sorted(harvested_emails):
        print(f" - {email}")
