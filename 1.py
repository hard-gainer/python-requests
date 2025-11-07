import requests

if __name__ == "__main__":
    resp = requests.get(url="https://jsonplaceholder.typicode.com/posts")
    posts = resp.json()[:5]

    for i, p in enumerate(posts, start=1):
        title = p.get("title", "<no title>")
        body = p.get("body", "<no body>")
        print(f"\nPost #{i} — title: {title}\n{body}")