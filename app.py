from flask import Flask, render_template, request, redirect, url_for
from utils.github_api import get_github_data

app = Flask(__name__)

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
    print(f'new message from {name} ({email}): {message}')
    return redirect(url_for('porfolio'))

if __name__ == "__main__":
    app.run(debug=True)
