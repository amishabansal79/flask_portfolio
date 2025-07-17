from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'  # app password if 2FA enabled

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]

    # Send email to your inbox
    msg = Message(subject=f"New Contact Form Submission: {subject}",
                  sender=email,
                  recipients=['your_email@gmail.com'])
    msg.body = f"""
    Name: {name}
    Email: {email}
    Subject: {subject}
    Message: {message}
    """

    mail.send(msg)

    flash("Thank you for contacting me. I will get back to you soon!", "success")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
