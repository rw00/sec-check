from flask import Flask, request, render_template, redirect, url_for, make_response
import os

app = Flask(__name__)
app.secret_key = "cookie-secret"

# In-memory storage for user data
users = {"johndoe": {"balance": 4200, "password": "securepass"}}


@app.route("/")
def index():
    user_id = request.cookies.get("user_id")
    if not user_id or user_id not in users:
        return redirect(url_for("login"))

    return render_template(
        "insecure/insecure_index.j2", user=users[user_id], username=user_id
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username]["password"] == password:
            response = make_response(redirect(url_for("index")))
            # VULNERABILITY: Setting cookie without SameSite=Strict or Lax
            # For modern browsers, we might need to explicitly set it to None.
            response.set_cookie("user_id", username)
            return response
        else:
            return render_template(
                "insecure/login.j2", error="Invalid username or password"
            )

    return render_template("insecure/login.j2")


@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for("login")))
    resp.delete_cookie("user_id")
    return resp


@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    user_id = request.cookies.get("user_id")
    if not user_id or user_id not in users:
        return "Unauthorized", 401

    if request.method == "POST":
        target = request.form.get("to")
        amount = int(request.form.get("amount", 0))
    else:
        # VULNERABILITY: State-changing action via GET
        target = request.args.get("to")
        amount = int(request.args.get("amount", 0))

    if amount > 0 and users[user_id]["balance"] >= amount:
        users[user_id]["balance"] -= amount
        print(f"Transferred {amount} to {target} from {user_id}")
        return redirect(url_for("index", success=f"Transferred ${amount} to {target}"))

    return "Insufficient funds or invalid amount", 400


if __name__ == "__main__":
    print("Insecure site starting on http://127.0.0.1:5001")
    app.run(debug=True, port=5001)
