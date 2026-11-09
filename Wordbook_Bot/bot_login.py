import os

import praw


def bot_login():
    required_vars = [
        "reddit_username",
        "reddit_password",
        "client_id",
        "client_secret",
    ]
    missing = [name for name in required_vars if not os.environ.get(name)]
    if missing:
        raise RuntimeError(
            "Missing Reddit environment variables: " + ", ".join(missing)
        )

    print("Logging in..")
    try:
        reddit = praw.Reddit(
            username=os.environ["reddit_username"],
            password=os.environ["reddit_password"],
            client_id=os.environ["client_id"],
            client_secret=os.environ["client_secret"],
            user_agent="kyle",
        )
        print("Logged in!")
        return reddit
    except Exception as exc:
        print("Failed to log in!")
        raise RuntimeError(f"Reddit login failed: {exc}") from exc
