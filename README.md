i havent added .env to .gitignore so it will be faster to test it for you, you need docker compose and makefile, commands:
- make test - run backend tests
- make start_dev - run compose development
- make start_dev_rebuil - run compose development and rebuild containers

The frontend starts at localhost:3000 and backend on localhost:8000
