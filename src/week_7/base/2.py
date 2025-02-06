import json

import requests


def process_user_data():
    url_posts = "https://jsonplaceholder.typicode.com/posts"
    url_comments = "https://jsonplaceholder.typicode.com/comments"
    url_users = "https://jsonplaceholder.typicode.com/users"

    response_posts = requests.get(url_posts)
    response_comments = requests.get(url_comments)
    response_users = requests.get(url_users)

    data_posts = response_posts.json()
    data_comments = response_comments.json()
    data_users = response_users.json()

    posts_count_with_user_id = {}

    for post in data_posts:
        user_id = post['userId']
        if user_id not in posts_count_with_user_id:
            posts_count_with_user_id[user_id] = 1
        else:
            posts_count_with_user_id[user_id] += 1

    comments_count_with_user_email = {}

    for comment in data_comments:
        email = comment['email']
        if email not in comments_count_with_user_email:
            comments_count_with_user_email[email] = 1
        else:
            comments_count_with_user_email[email] += 1

    statisticss = []
    for user in data_users:
        user_id = user["id"]
        user_email = user["email"]
        count_posts = posts_count_with_user_id.get(user_id)
        count_comments = comments_count_with_user_email.get(user_email)

        if count_comments is None:
            count_comments = 0

        static = {
            "id": user_id,
            "username": user["username"],
            "email": user["email"],
            "posts": count_posts,
            "comments": count_comments,
        }
        statisticss.append(static)

    res = {"statistics":statisticss}
    response  = requests.post("https://webhook.site/9de68c04-7a71-45ae-b598-e6ae209b285a", json=res)
    return response


print(process_user_data())

a = [{'id': 1, 'username': 'Bret', 'email': 'Sincere@april.biz', 'posts': 10, 'comments': 0},
     {'id': 2, 'username': 'Antonette', 'email': 'Shanna@melissa.tv', 'posts': 10, 'comments': 0}]
b = {"2": a}
print(b)
