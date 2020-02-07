run:
	docker-compose up -d api

stop:
	docker-compose down

test:
	python3 -m pytest tests/

run-heroku:
	python3 src/api.py

start:
	gunicorn src.api:app &


push-dockers:
	VERSION="1.0.0"
	docker tag python-pyramid rafaelleru/python-pyramid:1.0.0
	docker push rafaelleru/python-pyramid:1.0.0

	VERSION="1.0.0"
	docker tag stream-ai rafaelleru/stream-ai:1.0.0
	docker push rafaelleru/stream-ai:1.0.0

build-dockers:
	cp -r src ./docker/streamai
	docker build -t python-pyramid docker/pyramid
	docker build -t stream-ai docker/streamai

test-circleci:
	python3 src/api.py &
	python3 -m pytest tests/

create-gce-vm-terraform:
	cd terraform
	terraform apply

depliegue-gce:
	cd terraform
	terraform apply
	cd ..
	ansible-playbook provision/playbook.yml
	ansible-playbook despliegue/deploy.yml
