from pydantic import BaseSettings

from m3u8_daemon.version import __version__


class Config(BaseSettings):
    title: str
    version: str = __version__

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
