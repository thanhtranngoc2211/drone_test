from json import dumps
from httplib2 import Http
import os

build_number = os.getenv('BUILD_NUMBER')
commit = os.getenv('COMMIT')
project = os.getenv('PROJECT')
author = os.getenv('AUTHOR')

def main():
    """Google Chat incoming webhook quickstart."""
    url = "https://chat.googleapis.com/v1/spaces/AAAA96rxQ2I/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=hvSeDNTsFONz40n89_e-R8SnGVptn8oWVULNujvcB5M"
    app_message = {"text": f'User {author} triggered pipeline {build_number} - Commit: "{commit}" - Project: "{project}" completed!'}
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