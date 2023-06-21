FROM python:3.9-slim

WORKDIR /usr/src/app
# copy files/folders in celery_task to /usr/src/app
COPY ./src/celery_task ./celery_task/
COPY ./src/config ./

RUN pip install pandas celery flower python-dotenv
EXPOSE 5001
CMD ["celery","-A","celery_task.main","flower","--port=5001"]