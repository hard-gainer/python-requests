import requests
import sys
import json

if __name__ == "__main__":
    new_post = {"title": "foo", "body": "bar", "userId": 1}
    try:
        resp = requests.post(
            "https://jsonplaceholder.typicode.com/posts",
            data=new_post,
            timeout=10,
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}", file=sys.stderr)
        sys.exit(1)

    created = resp.json()
    post_id = created.get("id")
    print(f"Created post ID: {post_id}")
    print("Post content:")
    print(created)
