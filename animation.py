# Animation for UI

import sys
import time

BRIGHT_GREEN = "\033[92m"
RESET = "\033[0m"

def loading_animation() -> None:

    """
    Display a short loading animation in the console.
    """

    steps = [
        f"{BRIGHT_GREEN}Loading... ██□□□□□□□□ 20%",
        "Loading... ████□□□□□□ 40%",
        "Loading... ██████□□□□ 60%",
        "Loading... ████████□□ 80%",
        f"Loading... ██████████ 100%{RESET}"
    ]

    for step in steps:
        sys.stdout.write("\r" + step)
        sys.stdout.flush()
        time.sleep(0.2)

    time.sleep(0.3)

    sys.stdout.write("\r" + " " * 40 + "\r")
    sys.stdout.flush()