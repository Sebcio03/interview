start_dev:
	docker compose up 
start_dev_rebuild:
	docker compose up --build
test:
	docker exec -it local_backend pytest -s -vv $(ARGS)
