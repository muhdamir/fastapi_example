import os

from dotenv import load_dotenv

load_dotenv()

POST_URL = os.getenv("POST_URL")
COMMENT_URL = os.getenv("COMMENT_URL")
RABBITMQ_DEFAULT_USER = os.getenv("RABBITMQ_DEFAULT_USER")
RABBITMQ_DEFAULT_PASS = os.getenv("RABBITMQ_DEFAULT_PASS")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")
