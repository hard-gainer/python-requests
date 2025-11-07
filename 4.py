import requests
import sys

if __name__ == "__main__":
    new_post = {"title": "foo", "body": "bar", "userId": 1}

    try:
        resp = requests.post(
            "https://jsonplaceholder.typicode.com/posts",
            json=new_post,
            timeout=10,
        )
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}", file=sys.stderr)
        sys.exit(1)

    status = resp.status_code
    if status == 201:
        try:
            created = resp.json()
        except ValueError:
            print("Создано, но не удалось распарсить JSON ответа", file=sys.stderr)
            sys.exit(1)
        post_id = created.get("id")
        print(f"Created post ID: {post_id}")
        print("Post content:")
        print(created)
        sys.exit(0)
    elif status == 400:
        print("Ошибка 400: Bad Request — сервер считает данные некорректными.", file=sys.stderr)
        print("Response body:", resp.text, file=sys.stderr)
        sys.exit(1)
    elif status == 401:
        print("Ошибка 401: Unauthorized — требуется аутентификация.", file=sys.stderr)
        sys.exit(1)
    elif status == 403:
        print("Ошибка 403: Forbidden — доступ запрещён.", file=sys.stderr)
        sys.exit(1)
    elif status == 404:
        print("Ошибка 404: Not Found — конечная точка не найдена.", file=sys.stderr)
        sys.exit(1)
    elif 400 <= status < 500:
        print(f"Клиентская ошибка {status}.", file=sys.stderr)
        print("Response body:", resp.text, file=sys.stderr)
        sys.exit(1)
    elif 500 <= status < 600:
        print(f"Серверная ошибка {status}. Попробуйте позже.", file=sys.stderr)
        print("Response body:", resp.text, file=sys.stderr)
        sys.exit(1)
    else:
        print(f"Неожиданный код ответа: {status}", file=sys.stderr)
        print("Response body:", resp.text, file=sys.stderr)
        sys.exit(1)