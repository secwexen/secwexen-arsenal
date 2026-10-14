"""Provide the Secwexen Arsenal command-line interface banner."""

import os


def clear_screen() -> None:
    """Clear the terminal screen on Windows or Unix-like systems."""
    os.system("cls" if os.name == "nt" else "clear")


def print_banner() -> None:
    """Display the Secwexen Arsenal ASCII banner."""
    banner = r"""
   ███████╗███████╗ ██████╗██╗    ██╗███████╗██╗  ██╗███████╗███╗   ██╗
   ██╔════╝██╔════╝██╔════╝██║    ██║██╔════╝╚██╗██╔╝██╔════╝████╗  ██║
   ███████╗█████╗  ██║     ██║ █╗ ██║█████╗   ╚███╔╝ █████╗  ██╔██╗ ██║
   ╚════██║╚════╝  ██║     ██║███╗██║╚════╝   ██╔██╗ ╚════╝  ██║╚██╗██║
   ███████║███████╗╚██████╗╚███╔███╔╝███████╗██╔╝ ██╗███████╗██║ ╚████║
   ╚══════╝╚══════╝ ╚═════╝ ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
                             A R S E N A L
                Personal cybersecurity toolkit repository
    """

    print(banner)


def main() -> None:
    """Clear the terminal and display the application banner."""
    clear_screen()
    print_banner()


if __name__ == "__main__":
    main()
