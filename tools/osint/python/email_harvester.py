"""
email_harvester.py
Basic OSINT module to collect email addresses from a target domain.

Author: secwexen
"""

import re
import socket
from typing import Set, List
from urllib.parse import urljoin

import requests

from utils import log_info, log_warning, log_error, is_valid_email


EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
DEFAULT_PATHS = [
    "/",
    "/contact",
    "/contact-us",
    "/about",
    "/about-us",
    "/team",
    "/staff",
    "/support",
    "/help",
]


def _normalize_domain(domain: str) -> str:
    domain = domain.strip()
    if domain.startswith("http://") or domain.startswith("https://"):
        domain = domain.split("://", 1)[1]
    return domain.rstrip("/")


def _build_urls(domain: str, paths: List[str]) -> List[str]:
    urls = []

    for scheme in ("https://", "http://"):
        base = f"{scheme}{domain}"
        for path in paths:
            urls.append(urljoin(base, path))

    return urls


def _fetch_url(url: str, timeout: int = 10) -> str | None:
    try:
        resp = requests.get(url, timeout=timeout, verify=True, allow_redirects=True)
        if resp.status_code >= 200 and resp.status_code < 400:
            return resp.text
        log_warning(f"[OSINT] Non-success status for {url}: {resp.status_code}")
    except requests.RequestException as e:
        log_warning(f"[OSINT] Failed to fetch {url}: {e}")
    return None


def _extract_emails_from_text(text: str) -> Set[str]:
    emails = set(EMAIL_REGEX.findall(text or ""))
    # Basic cleanup & validation
    cleaned = {email.strip().strip(".,;:") for email in emails}
    return {e for e in cleaned if is_valid_email(e)}


def _filter_domain_emails(emails: Set[str], domain: str) -> Set[str]:
    domain = _normalize_domain(domain)
    return {e for e in emails if e.lower().endswith("@" + domain.lower())}


def _resolve_domain(domain: str) -> str | None:
    try:
        ip = socket.gethostbyname(domain)
        log_info(f"[OSINT] Resolved {domain} to {ip}")
        return ip
    except socket.gaierror:
        log_warning(f"[OSINT] Could not resolve domain: {domain}")
        return None


def harvest_emails(domain: str, only_domain: bool = True) -> Set[str]:
    """
    Harvest email addresses from common pages of a target domain.

    :param domain: Target domain (e.g., 'example.com')
    :param only_domain: If True, only return emails matching the domain
    :return: Set of unique email addresses
    """
    domain = _normalize_domain(domain)
    log_info(f"[OSINT] Starting email harvest for: {domain}")

    _resolve_domain(domain)

    urls = _build_urls(domain, DEFAULT_PATHS)
    all_emails: Set[str] = set()

    for url in urls:
        log_info(f"[OSINT] Fetching: {url}")
        html = _fetch_url(url)
        if not html:
            continue

        emails = _extract_emails_from_text(html)
        if emails:
            log_info(f"[OSINT] Found {len(emails)} email(s) on {url}")
            all_emails.update(emails)

    if only_domain:
        all_emails = _filter_domain_emails(all_emails, domain)

    if not all_emails:
        log_warning(f"[OSINT] No emails found for domain: {domain}")
    else:
        log_info(f"[OSINT] Harvest completed. Total unique emails: {len(all_emails)}")

    return all_emails


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python email_harvester.py <domain>")
        sys.exit(1)

    target_domain = sys.argv[1]
    emails = harvest_emails(target_domain)

    print(f"\n[OSINT] Emails found for {target_domain}:")
    for e in sorted(emails):
        print(f" - {e}")
