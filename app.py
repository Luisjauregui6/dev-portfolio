from flask import Flask, render_template, request
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
    return render_template("portfolio.html", data=data, hint=hint)

if __name__ == "__main__":
    app.run(debug=True)
