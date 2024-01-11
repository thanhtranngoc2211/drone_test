FROM python:3-slim

ENV DRONE_BUILD_NUMBER=0
ENV DRONE_COMMIT='unknown commit'
ENV DRONE_REPO='unknown project'
ENV DRONE_COMMIT_AUTHOR_EMAIL='octocat@github.com'

WORKDIR /code

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY webhook.py .

ENTRYPOINT ["python"]
CMD ["webhook.py"]