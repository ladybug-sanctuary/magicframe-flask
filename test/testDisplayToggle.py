import time

import requests


URL="http://localhost"  # or .local network address
PORT="8081"


def toggle_display(display_state: str):
    requests.post(f"{URL}:{PORT}", data={"toggle": f"Turn display {display_state}"})


def main():
    toggle_display("off")
    time.sleep(5)  # wait 5 seconds
    toggle_display("on")


if __name__ == "__main__":
    main()
