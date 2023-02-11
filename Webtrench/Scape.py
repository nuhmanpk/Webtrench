import requests

def is_scrapable(url):
    response = requests.head(url)
    if response.status_code == 200:
        x_robots_tag = response.headers.get("X-Robots-Tag", "")
        if "noindex" in x_robots_tag or "nofollow" in x_robots_tag:
            return False
        else:
            return True
    else:
        return False
