FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN pip install --upgrade pip

COPY ./requirements.txt ./requirements.txt

RUN pip install -r  ./requirements.txt

RUN mkdir /service

WORKDIR /service

COPY ./app /service/app