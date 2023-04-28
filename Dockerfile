ARG python=python:3.9-alpine

FROM ${python} as build
WORKDIR /code

COPY requirements.txt .
RUN python3 -m venv /venv
ENV PATH=/venv/bin:$PATH

RUN apk update  \
    && pip3 install --upgrade pip \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev supervisor openssl-dev build-base \
    && pip3 install --no-cache-dir --upgrade  -r requirements.txt


FROM ${python}
COPY --from=build /venv /venv
WORKDIR /code
ENV PATH=/venv/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk --no-cache --update add libffi libressl postgresql-libs gcc libc-dev

COPY . .

CMD ["python3", "app/main.py"]