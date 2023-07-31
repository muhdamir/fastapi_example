FROM python:3.9-slim

WORKDIR /usr/src/app
# copy files/folders in celery_task to /usr/src/app
COPY ./src/celery_task ./celery_task/
COPY ./src/config ./config/
COPY ./requirements_celery.txt ./

RUN pip install -r requirements_celery.txt

CMD ["celery","-A","celery_task.main","worker","-l","INFO"]