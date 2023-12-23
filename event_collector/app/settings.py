from dotenv import find_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    app_port: int = Field(8000, env='EVENT_COLLECTOR_PORT')
    app_host: str = Field('localhost', env='EVENT_COLLECTOR_HOST')
    kafka_url: str = Field(..., env='KAFKA_URL')
    kafka_topic: str = Field(..., env='KAFKA_TOPIC')

    class Config:
        env_file = find_dotenv('.env')
        env_file_encoding = 'utf-8'
        extra = 'ignore'
