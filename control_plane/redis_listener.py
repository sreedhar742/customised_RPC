import json
import redis

from control_plane.registry import ServiceRegistry

class RedisListener:

    def __init__(self, registry: ServiceRegistry):
        self.registry = registry

        self.redis = redis.Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )

    def start(self):
        pubsub = self.redis.pubsub()

        pubsub.subscribe("service_updates")

        print("Listening on Redis channel: service_updates")

        for message in pubsub.listen():

            if message["type"] != "message":
                continue

            try:
                event = json.loads(message["data"])

                service = event["service"]
                action = event["action"]
                endpoint = event["endpoint"]

                print(f"\nReceived Event: {event}")

                if action == "ADD":
                    self.registry.add_endpoint(service, endpoint)

                elif action == "REMOVE":
                    self.registry.remove_endpoint(service, endpoint)

                self.registry.print_registry()

            except Exception as e:
                print("Error:", e)
