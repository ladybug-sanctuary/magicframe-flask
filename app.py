#!/usr/bin/env python3
"""Flask front-end app for magicframe"""

from flask import Flask


HOST="0.0.0.0"
PORT=8081

app = Flask(__name__)


@app.route("/")
def toggle():
    return "<h1>MagicFrame</h1>"


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
