run:
	docker-compose up -d api

stop:
	docker-compose down

test:
	python3 -m pytest tests/

test-circleci:
	python3 src/api.py &
	python3 -m pytest tests/

