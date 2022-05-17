### GST Tax Management API's

#### Getting Started

1. Download and Install docker and docker-compose to run the apis
2. Run ```docker-compose up```
3. This command will setup the FastAPI container, PostgreSQL database and Adminer tool(GUI for database)
4. Once docker is done with building the image it will produce logs in the terminal
5. You should be able to see ```Uvicorn running on http://0.0.0.0:8000```
6. Head to ```http://127.0.0.1:8000``` in your machine and you should be able to see 
7. ```{"detail": "Not Found"}```
8. Head to ```http://127.0.0.1:8000/docs``` for the documentation and to test the feature of the API


### Tests

1. All the tests are located in tests folder in backend directory and
2. The tests are run through pytest

Thank you 