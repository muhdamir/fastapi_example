FROM python:3.9-slim

WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./src ./

# WORKDIR /usr/src/app/src

EXPOSE 8000
#  Uvicorn to not care about the incoming host IP with option --host 0.0.0.0
CMD ["uvicorn","main:app","--host" ,"0.0.0.0", "--port","8000"]


