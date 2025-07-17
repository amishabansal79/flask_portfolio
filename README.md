# 🌟 Amisha Bansal – Portfolio Website

This is my **personal portfolio website** built using **Flask** and styled with **Tailwind CSS CDN**. It showcases my projects, skills, certifications, education, and contact details in a responsive design.

---

## 🔗 **Live Demo**

[View Website](https://flask-portfolio-kqo3.onrender.com/)

---

## 📌 **Features**

- Clean hero section with introduction
- About me section
- Skills and technologies
- Projects with GitHub links
- Certifications timeline
- Education details
- Contact section with form layout
- Contact form integrated with **Flask-Mail** to receive emails directly

---

## 🛠️ **Tech Stack**

- **Frontend:** HTML, CSS, Tailwind CSS CDN
- **Backend:** Flask (Python), Flask-Mail
- **Deployment:** Render

---

## 🚀 **Setup Locally**

1. **Clone this repository**

    ```bash
    git clone https://github.com/amishabansal79/flask_portfolio.git
    cd flask_portfolio
    ```

2. **Create a virtual environment and activate it**

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**

    Create a `.env` file (or set them directly) with your email credentials for Flask-Mail:

    ```
    MAIL_USERNAME=your_email@gmail.com
    MAIL_PASSWORD=your_app_password
    ```

5. **Run the app**

    ```bash
    python app.py
    ```

6. **Visit**

    ```
    http://127.0.0.1:5000/
    ```

---

## ✉️ **Contact Form Email Integration**

This project uses **Flask-Mail** to send form submissions to your email address securely.

---

## 💡 **Future Improvements**

- Add database integration for storing contact messages
- Dynamic projects section using backend data
- Animations and interactive UI improvements

---

## 📄 **License**

This project is open-source and free to use for learning and portfolio building.

---
