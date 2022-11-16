from m3u8_daemon.api import Api
from m3u8_daemon.core.config import Config
from m3u8_daemon.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api
