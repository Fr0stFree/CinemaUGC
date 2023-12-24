from typing import Literal

from dotenv import find_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    selected_broker: Literal['kafka', 'rabbitmq'] = Field(..., env='SELECTED_BROKER')
    kafka_url: str = Field(..., env='KAFKA_URL')
    kafka_topic: str = Field(..., env='KAFKA_TOPIC')
    rabbitmq_host: str = Field(..., env='RABBITMQ_HOST')
    rabbitmq_port: int = Field(..., env='RABBITMQ_PORT')
    rabbitmq_username: str = Field(..., env='RABBITMQ_USERNAME')
    rabbitmq_password: str = Field(..., env='RABBITMQ_PASSWORD')
    rabbitmq_exchange: str = Field(..., env='RABBITMQ_EXCHANGE')
    rabbitmq_queue_name: str = Field(..., env='RABBITMQ_QUEUE_NAME')

    class Config:
        env_file = find_dotenv('.env')
        env_file_encoding = 'utf-8'
        extra = 'ignore'
