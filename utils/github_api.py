import requests
import os

def _get_headers():
    token = os.environ.get('GITHUB_TOKEN', '').strip()
    headers = {
        "Accept": "application/vnd.github.mercy-preview+json"
    }
    if token:
        
        headers["Authorization"] = f"token {token}"
    return headers

def get_github_data(username):
    headers = _get_headers()
    user_url = f'https://api.github.com/users/{username}'
    repos_url = f'https://api.github.com/users/{username}/repos'

    try:
        user_resp = requests.get(user_url, headers=headers)
        repos_resp = requests.get(repos_url, headers=headers)

        
        print('USER RESPONSE:', user_resp.status_code)
        print('REPOS RESPONSE:', repos_resp.status_code)

        
        if user_resp.status_code == 401 or repos_resp.status_code == 401:
            return {
                'name': username,
                'bio': 'GitHub authentication failed (bad token).',
                'avatar': None,
                'html_url': f'https://github.com/{username}',
                'repos': []
            }

        # Rate limit
        if user_resp.status_code == 403 or repos_resp.status_code == 403:
            return {
                'name': username,
                'bio': 'GitHub API rate limit reached. Try again later.',
                'avatar': None,
                'html_url': f'https://github.com/{username}',
                'repos': []
            }

        user = user_resp.json()
        repos = repos_resp.json()
        if not isinstance(repos, list):
            repos = []
    except Exception as e:
        print('Exception in get_github_data:', e)
        user, repos = {}, []

    top_repos = sorted(repos, key=lambda r: r.get('stargazers_count', 0), reverse=True)[:5]
    repo_list = []

    for r in top_repos:
        try:
            topics_resp = requests.get(r['url'] + '/topics', headers=_get_headers())
            topics_json = topics_resp.json()
            topics = topics_json.get('names', [])
        except Exception:
            topics = []

        if not topics:
            lang = (r.get('language') or "").lower()
            topics = [lang] if lang else []

        repo_list.append({
            'name': r.get('name'),
            'description': r.get('description'),
            'stars': r.get('stargazers_count'),
            'url': r.get('html_url'),
            'tags': topics
        })

    return {
        'name': user.get('name') or username,
        'bio': user.get('bio') or "No bio available",
        'avatar': user.get('avatar_url'),
        'html_url': user.get('html_url') or f'https://github.com/{username}',
        'repos': repo_list
    }