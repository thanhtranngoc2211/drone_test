FROM python:3-slim

ENV BUILD_NUMBER=0
ENV COMMIT='unknown commit'
ENV PROJECT='unknown project'
ENV AUTHOR_EMAIL='octocat@github.com'

WORKDIR /code

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY webhook.py .

CMD ["python", "webhook.py"]