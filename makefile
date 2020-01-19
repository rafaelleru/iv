run:
	docker-compose up -d api

stop:
	docker-compose down

test:
	python3 -m pytest tests/
