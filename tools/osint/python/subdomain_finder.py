"""Discover subdomains using DNS resolution and optional HTTP checks."""

import socket
import sys
from typing import List

import requests

from utils import log_info, log_warning


DEFAULT_WORDLIST = [
    "www",
    "mail",
    "ftp",
    "dev",
    "api",
    "test",
    "stage",
    "staging",
    "admin",
    "panel",
    "blog",
    "shop",
    "cdn",
    "assets",
]


def _normalize_domain(domain: str) -> str:
    """Normalize a domain by removing its scheme and trailing slashes."""
    normalized_domain = domain.strip().lower()

    if normalized_domain.startswith(("http://", "https://")):
        normalized_domain = normalized_domain.split("://", 1)[1]

    return normalized_domain.rstrip("/")


def _resolve_dns(host: str) -> str | None:
    """Resolve a hostname to an IPv4 address, or return None on failure."""
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return None


def _http_check(url: str, timeout: int = 5) -> bool:
    """Check whether a URL returns an HTTP response below status 500."""
    try:
        response = requests.get(
            url,
            timeout=timeout,
            verify=True,
        )
        return response.status_code < 500

    except requests.RequestException:
        return False


def _build_subdomains(domain: str, wordlist: List[str]) -> List[str]:
    """Generate candidate subdomains from a domain and wordlist."""
    return [
        f"{word}.{domain}"
        for word in wordlist
    ]


def find_subdomains(
    domain: str,
    wordlist: List[str] | None = None,
    http_verify: bool = True,
) -> dict[str, dict[str, str | bool]]:
    """Find resolvable subdomains and optionally check their HTTP services."""
    normalized_domain = _normalize_domain(domain)

    log_info(
        f"[OSINT] Starting subdomain scan for: {normalized_domain}"
    )

    if wordlist is None:
        wordlist = DEFAULT_WORDLIST

    subdomains = _build_subdomains(normalized_domain, wordlist)
    results: dict[str, dict[str, str | bool]] = {}

    for subdomain in subdomains:
        log_info(f"[OSINT] Resolving: {subdomain}")
        ip_address = _resolve_dns(subdomain)

        if not ip_address:
            continue

        log_info(
            f"[OSINT] Found: {subdomain} -> {ip_address}"
        )

        http_ok = False

        if http_verify:
            for scheme in ("https://", "http://"):
                url = f"{scheme}{subdomain}"

                if _http_check(url):
                    http_ok = True
                    break

        results[subdomain] = {
            "ip": ip_address,
            "http": http_ok,
        }

    if not results:
        log_warning(
            f"[OSINT] No subdomains found for {normalized_domain}"
        )
    else:
        log_info(
            "[OSINT] Subdomain scan completed. "
            f"Found {len(results)} active subdomain(s)."
        )

    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python subdomain_finder.py <domain>")
        sys.exit(1)

    target_domain = sys.argv[1]
    discovered_subdomains = find_subdomains(target_domain)

    print(f"\n[OSINT] Active subdomains for {target_domain}:")

    for subdomain_name, info in discovered_subdomains.items():
        http_status = "Yes" if info["http"] else "No"

        print(
            f" - {subdomain_name} "
            f"({info['ip']}) HTTP: {http_status}"
        )
