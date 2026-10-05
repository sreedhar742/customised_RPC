from control_plane.registry import ServiceRegistry
from control_plane.redis_listener import RedisListener
registry = ServiceRegistry()

listener = RedisListener(registry)

listener.start()

