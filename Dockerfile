FROM python:3

ENV PYTHONUNBUFFERED 1
# Default environment
ENV ENV development

RUN mkdir -p /challenge_newcombin
WORKDIR /challenge_newcombin

# RUN apt-get update -y
# RUN apt-get install build-essential -y

# This command is neccesary to update dependencies before build the container
# pipenv run pip freeze > requirements.txt

COPY requirements.txt /challenge_newcombin/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /challenge_newcombin

CMD [ "python" ]