from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# In-memory storage for comments (like a DB)
comments = [
    {
        "author": "Admin",
        "text": "Welcome to RW Demo Labs! Leave comments below.",
    },
    {"author": "John", "text": "Great site! Thanks for the info!"},
]


@app.route("/")
def index():
    # VULNERABILITY: Rendering the comments directly.
    return render_template("index.j2", comments=comments)


@app.route("/post_comment", methods=["POST"])
def post_comment():
    author = request.form.get("author", "Anonymous")
    text = request.form.get("text")

    if text:
        # VULNERABILITY: No sanitization
        comments.append({"author": author, "text": text})

    return redirect(url_for("index"))


if __name__ == "__main__":
    print("Starting server on http://127.0.0.1:5005")
    app.run(debug=True, port=5005)
