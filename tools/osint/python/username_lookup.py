"""Check public profile URLs for a username across supported platforms."""

import sys
from typing import Dict
from urllib.parse import quote

import requests

from utils import log_info, log_warning


PLATFORMS: Dict[str, str] = {
    "GitHub": "https://github.com/{user}",
    "GitLab": "https://gitlab.com/{user}",
    "Twitter": "https://x.com/{user}",
    "Medium": "https://medium.com/@{user}",
    "HackerOne": "https://hackerone.com/{user}",
}


def _check_profile(url: str, timeout: int = 8) -> bool:
    """Return whether a profile URL appears to be accessible."""
    try:
        response = requests.get(
            url,
            timeout=timeout,
            allow_redirects=True,
        )

        if response.status_code == 200:
            return True

        if (
            response.status_code in (301, 302)
            and "login" not in response.text.lower()
        ):
            return True

    except requests.RequestException as exc:
        log_warning(f"[OSINT] Request failed for {url}: {exc}")

    return False


def lookup_username(username: str) -> Dict[str, str]:
    """Check a username against the configured public profile URLs."""
    normalized_username = username.strip().lstrip("@")

    if not normalized_username:
        log_warning("[OSINT] Username cannot be empty.")
        return {}

    log_info(
        f"[OSINT] Starting username lookup for: "
        f"{normalized_username}"
    )

    encoded_username = quote(normalized_username, safe="")
    results: Dict[str, str] = {}

    for platform_name, url_template in PLATFORMS.items():
        url = url_template.format(user=encoded_username)

        log_info(f"[OSINT] Checking {platform_name}: {url}")

        if _check_profile(url):
            log_info(f"[OSINT] FOUND on {platform_name}")
            results[platform_name] = url
        else:
            results[platform_name] = "Not Found"

    found_count = sum(
        1
        for status in results.values()
        if status != "Not Found"
    )

    if found_count == 0:
        log_warning(
            "[OSINT] No profiles found for username: "
            f"{normalized_username}"
        )
    else:
        log_info(
            "[OSINT] Username lookup completed. "
            f"Found on {found_count} platform(s)."
        )

    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python username_lookup.py <username>")
        sys.exit(1)

    target_username = sys.argv[1]
    lookup_results = lookup_username(target_username)

    print(f"\n[OSINT] Results for username '{target_username}':")

    for service_name, status in lookup_results.items():
        print(f" - {service_name}: {status}")
