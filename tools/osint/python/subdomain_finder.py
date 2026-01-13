"""
subdomain_finder.py
OSINT module to discover subdomains using DNS resolution
and optional HTTP validation.

Author: secwexen
"""

import socket
import requests
from typing import List, Set

from utils import log_info, log_warning, log_error


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
    domain = domain.strip().lower()
    if domain.startswith("http://") or domain.startswith("https://"):
        domain = domain.split("://", 1)[1]
    return domain.rstrip("/")


def _resolve_dns(host: str) -> str | None:
    try:
        ip = socket.gethostbyname(host)
        return ip
    except socket.gaierror:
        return None


def _http_check(url: str, timeout: int = 5) -> bool:
    try:
        resp = requests.get(url, timeout=timeout, verify=True)
        return resp.status_code < 500
    except requests.RequestException:
        return False


def _build_subdomains(domain: str, wordlist: List[str]) -> List[str]:
    return [f"{w}.{domain}" for w in wordlist]


def find_subdomains(domain: str, wordlist: List[str] | None = None, http_verify: bool = True) -> dict:
    """
    Discover subdomains using DNS resolution and optional HTTP validation.

    :param domain: Target domain (e.g., example.com)
    :param wordlist: Custom wordlist (optional)
    :param http_verify: Whether to send HTTP requests to verify active hosts
    :return: Dict mapping subdomain -> {ip, http}
    """
    domain = _normalize_domain(domain)
    log_info(f"[OSINT] Starting subdomain scan for: {domain}")

    if wordlist is None:
        wordlist = DEFAULT_WORDLIST

    subdomains = _build_subdomains(domain, wordlist)
    results = {}

    for sub in subdomains:
        log_info(f"[OSINT] Resolving: {sub}")
        ip = _resolve_dns(sub)

        if not ip:
            continue

        log_info(f"[OSINT] Found: {sub} -> {ip}")

        http_ok = False
        if http_verify:
            for scheme in ("https://", "http://"):
                url = f"{scheme}{sub}"
                if _http_check(url):
                    http_ok = True
                    break

        results[sub] = {
            "ip": ip,
            "http": http_ok,
        }

    if not results:
        log_warning(f"[OSINT] No subdomains found for {domain}")
    else:
        log_info(f"[OSINT] Subdomain scan completed. Found {len(results)} active subdomain(s).")

    return results


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python subdomain_finder.py <domain>")
        sys.exit(1)

    target = sys.argv[1]
    found = find_subdomains(target)

    print(f"\n[OSINT] Active subdomains for {target}:")
    for sub, info in found.items():
        print(f" - {sub} ({info['ip']}) HTTP: {'Yes' if info['http'] else 'No'}")
