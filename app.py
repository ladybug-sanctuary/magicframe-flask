#!/usr/bin/env python3
"""Flask front-end app for magicframe"""

from flask import Flask, render_template, request


HOST="0.0.0.0"
PORT=8081

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def toggle():
    if request.method == "GET":
        pass

    if request.method == "POST":
        pass

    return render_template("index.html", toggle_message="Turn display on/off")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
