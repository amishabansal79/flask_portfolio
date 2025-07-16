from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # needed for flashing messages

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]

    # Example: Print in terminal (you can integrate SMTP to send email)
    print(f"New message from {name} ({email})")
    print(f"Subject: {subject}")
    print(f"Message: {message}")

    flash("Thank you for contacting me. I will get back to you soon!", "success")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
