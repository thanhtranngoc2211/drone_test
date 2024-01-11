from json import dumps
from httplib2 import Http
import os

build_number = os.getenv('DRONE_BUILD_NUMBER')
commit = os.getenv('DRONE_COMMIT')
project = os.getenv('DRONE_REPO')
author = os.getenv('DRONE_COMMIT_AUTHOR_EMAIL')

def main():
    """Google Chat incoming webhook quickstart."""
    url = "https://chat.googleapis.com/v1/spaces/AAAA96rxQ2I/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=hvSeDNTsFONz40n89_e-R8SnGVptn8oWVULNujvcB5M"
    app_message = {"text": f'Pipeline {build_number} - Commit: "{commit}" - Project: "{project}" completed!\nTriggered by {author}'}
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(app_message),
    )
    print(response)


if __name__ == "__main__":
    main()