FROM python-pyramid

CMD mkdir /app

COPY . /app

EXPOSE 8000

WORKDIR /app

ENV PYTHONPATH=/app

CMD python src/api.py
