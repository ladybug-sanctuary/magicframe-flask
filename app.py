#!/usr/bin/env python3
"""Flask front-end app for magicframe"""

from flask import Flask, redirect, render_template, request, url_for

import vcgencmd


HOST="0.0.0.0"
PORT=8081

app = Flask(__name__, template_folder="templates", static_folder="static")


def on_or_off(newstatus: int) -> str:
    return "on" if newstatus else "off"


@app.route("/", methods=["GET", "POST"])
def toggle():
    if request.method == "GET":
        newstatus = vcgencmd.get_status() ^ 1  # 1 or 0
        return render_template("index.html", on_or_off=on_or_off(newstatus))

    if request.method == "POST":
        if "toggle" in request.form:
            oldmsg = request.form.get("toggle")  # previous value of toggle_message
            action = oldmsg.split()[-1]
            newstatus = 1 if action.lower() == "on" else 0  # "on" vs "off"
            vcgencmd.set_status(newstatus)
            return redirect(url_for("toggle"))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
