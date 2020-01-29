FROM python

ADD config/requirements.txt /etc/requirements.txt

RUN pip install -r /etc/requirements.txt

CMD mkdir /app

COPY . /app

EXPOSE 8000

WORKDIR /app

ENV PYTHONPATH=/app

CMD python src/api.py
