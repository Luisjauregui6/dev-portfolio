from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os
from utils.github_api import get_github_data

app = Flask(__name__)
app.secret_key = os.environ.get('secret_key', 'dev')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_POST'] = 587
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
            if username.lower() == 'luisjauregui6':
                data['is_owner'] = True
            else:
                data['is_owner'] = False   

    return render_template("portfolio.html", data=data, hint=hint)

# contact form 
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    try: 
        msg = Message(
            subject = f'new message from {name}',
            sender = email,
            recipients = ['luisjauregui221@gmail.com'],
            body = f'name: {name}\nEmail: {email}\n\nMessage: {message}'
        )
        mail.send(msg)
        flash('message sent!', 'success')
    except Exception as e:
        flash(f'error while trying to send the message: {e}', 'danger')

    return redirect(url_for('portfolio'))

if __name__ == "__main__":
    app.run(debug=False)
