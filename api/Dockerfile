FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV DATABASE_URL=postgresql+psycopg2://$POSTGRES_USER:$POSTGRES_PASSWORD@postgres_db:5432/$POSTGRES_DB

RUN pip install --upgrade pip

WORKDIR /code

ADD ./requirements.txt /code/
RUN pip3 install --no-cache-dir -r requirements.txt

ADD . /code