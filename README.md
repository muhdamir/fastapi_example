# An example of FastAPI application
#### Prepared by: Amirul
An example of fastapi application with the idea of implementing the `Onion` architecture. Though this repo may not be the perfect implemetation of the said architecture style, but still it's a good start.

To run the project in your local machine, first you need to install all the required libraries:

```
pip install -r requirements.txt
```


then simply go into src folder:
```bash
cd ./src
```


then type this command:
```bash
uvicorn app:main
```


By default, the FastAPI app will be running on port `8000` at localhost.
So, to open the swaggerUI, you need to open this link `http://localhost:8000/docs` 
