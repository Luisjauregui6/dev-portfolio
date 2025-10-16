# Dev Portfolio
A personal GitHub portfolio web app to search GitHub profiles, view their repositories, & display each project's dynamic tags. Built with Python, Flask & Bootstrap. 

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=flat-square&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Jinja2](https://img.shields.io/badge/Jinja2-BA8B00?style=flat-square&logo=jinja&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub%20REST%20API-v3-181717?style=flat-square&logo=github&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.x-3C8DBC?style=flat-square&logo=python&logoColor=white)

![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)



## Features
- Search for any GitHub user by their username
- Display their profile info: avatar, name, bio, repos, etc.
- Responsive design using Bootstrap 5

## Tech Stack
- **Frontend:** HTML, CSS, Bootstrap 5, JavaScript
- **Backend:** Python 3.x, Flask, Jinja2
- **API:** GitHub REST API V3
- **Other Libraries:** `requests`


## Installation

```bash
# Clone repository
git clone https://github.com/Luisjauregui6/dev-portfolio.git
cd dev-portfolio

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# MacOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
1. Run the Flask app:
  ```bash
  python app.py
   ```
2. Open your browser at `http://127.0.0.1:5000`

3. Enter a GitHub username in the search bar

4. View profile and repositories with dynamic tags

5. Click the Hint button if needed   


## Project Structure
```text
dev-portfolio/
├── app.py
├── utils/
│   └── github_api.py
├── templates/
│   └── portfolio.html
├── static/
│   └── style.css
└── venv/
```

## Screenshots
> EMPTY PLEASE UPLOAD SCREENSHOTS ONCE YOU ARE DONE WITH THE PROJECT

## Contributing
Contributions are welcome! If you’d like to improve this project, feel free to fork the repository, make your changes, and submit a pull request.

## License

MIT License


