#!/usr/bin/env python3
"""Flask front-end app for magicframe"""

from flask import Flask, render_template, request

import vcgencmd


HOST="0.0.0.0"
PORT=8081

app = Flask(__name__, template_folder="templates")


def turn_display(newstatus: int) -> str:
    return "Turn display " + ("on" if newstatus else "off")


@app.route("/", methods=["GET", "POST"])
def toggle():
    if request.method == "GET":
        newstatus = vcgencmd.get_status() ^ 1  # 1 or 0
        return render_template("index.html", toggle_message=turn_display(newstatus))

    if request.method == "POST":
        if "toggle" in request.form:
            oldmsg = request.form.get("toggle")  # previous value of toggle_message
            action = oldmsg.split()[-1]
            newstatus = 1 if action == "on" else 0  # "on" vs "off"
            vcgencmd.set_status(newstatus)
            newstatus = int(newstatus) ^ 1  # flip after executing command
            return render_template("index.html", toggle_message=turn_display(newstatus))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
