FROM python:3.7-slim
LABEL maintainer = "rictegao@gmail.com"

#Project path
RUN mkdir /usr/app
WORKDIR /usr/app
ADD . /usr/app

# Install dependencies
RUN pip3 install -r requirements.txt

#install spacy md wordvec
RUN python -m spacy download en_core_web_md