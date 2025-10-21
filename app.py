from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import logging

# Load local .env for development only
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("GITHUB_TOKEN present? %s", bool(os.environ.get("GITHUB_TOKEN")))

from utils.github_api import get_github_data

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev')

# Mail config 
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USER')

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def portfolio():
    data = None
    hint = "Try: Luisjauregui6"
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            data = get_github_data(username)
           
            if isinstance(data, dict):
                data['is_owner'] = (username.lower() == 'luisjauregui6')
    return render_template("portfolio.html", data=data, hint=hint)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    try:
        msg = Message(
            subject=f'new message from {name}',
            sender=os.environ.get('EMAIL_USER'),
            recipients=['luisjauregui221@gmail.com'],
            body=f'name: {name}\nEmail: {email}\n\nMessage: {message}'
        )
        mail.send(msg)
        flash('message sent!', 'success')
    except Exception as e:
        logger.exception("Error sending mail")
        flash(f'error while trying to send the message: {e}', 'danger')
    return redirect(url_for('portfolio'))


@app.route('/_health')
def healthcheck():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')