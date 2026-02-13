from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    # This page will contain a hidden form that auto-submits to the insecure site
    return render_template("jackpot/jackpot_index.j2")


if __name__ == "__main__":
    print("Jackpot site starting on http://127.0.0.1:5002")
    app.run(debug=True, port=5002)
