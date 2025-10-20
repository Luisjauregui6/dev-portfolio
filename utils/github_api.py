import requests

HEADERS = {"Accept": "application/vnd.github.mercy-preview+json"}

def get_github_data(username):
    user_url = f'https://api.github.com/users/{username}'
    repos_url = f'https://api.github.com/users/{username}/repos'

    user_resp = requests.get(user_url, headers=HEADERS).json()
    repos_resp = requests.get(repos_url, headers=HEADERS).json()

    try:
        user = requests.get(user_url, headers=HEADERS).json()
    except Exception:
        user = {}    

    try:
        repos = requests.get(repos_url, headers=HEADERS).json()
        if not isinstance(repos, list):
            repos = []
    except Exception:
        repos = []               

    top_repos = sorted(repos, key=lambda r: r.get('stargazers_count', 0), reverse=True)[:5]

    repo_list = []
    for r in top_repos:
        topics = []
        try:
          topics_resp = requests.get(r['url'] + '/topics', headers=HEADERS)
          topics_json = topics_resp.json()
          topics = topics_json.get('names', [])
        except Exception:
            topics = []  
       
        if not topics:
            topics = []
            lang = (r.get('language') or "").lower()
            if lang:
                topics.append(lang)

        repo_list.append({
            'name': r.get('name'),
            'description': r.get('description'),
            'stars': r.get('stargazers_count'),
            'url': r.get('html_url'),
            'tags': topics  
        })

    return {
        'name': user.get('name'),
        'bio': user.get('bio') or "No bio available",
        'avatar': user.get('avatar_url'),
        'html_url': user.get('html_url'),
        'repos': repo_list
    }
