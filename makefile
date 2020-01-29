run:
	docker-compose up -d api

stop:
	docker-compose down

test:
	python3 -m pytest tests/

run-heroku:
	python3 src/api.py

push-dockers:
	# contenedor base con las dependencias de pyramid para usar en desarrollo
	VERSION="1.0.0"
	docker tag python-pyramid rafaelleru/python-pyramid:$VERSION
	docker push rafaelleru/python-pyramid:$VERSION

	VERSION="1.0.0"
	docker tag stream-ai rafaelleru/stream-ai:$VERSION
	docker push rafaelleru/stream-ai:$VERSION

build-dockers:
	cp -r src ./docker/streamai
	docker build -t python-pyramid docker/pyramid
	docker build -t stream-ai docker/streamai

test-circleci:
	python3 src/api.py &
	python3 -m pytest tests/
