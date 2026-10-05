from threading import Lock


class ServiceRegistry:
    def __init__(self):
        # {
        #     "backend": {
        #         "172.18.0.5:8000",
        #         "172.18.0.6:8000"
        #     }
        # }
        self._services = {}
        self._lock = Lock()

    def add_endpoint(self, service_name: str, endpoint: str):
        with self._lock:
            if service_name not in self._services:
                self._services[service_name] = set()

            self._services[service_name].add(endpoint)

    def remove_endpoint(self, service_name: str, endpoint: str):
        with self._lock:
            if service_name not in self._services:
                return

            self._services[service_name].discard(endpoint)

            if len(self._services[service_name]) == 0:
                del self._services[service_name]

    def get_endpoints(self, service_name: str):
        with self._lock:
            return list(self._services.get(service_name, set()))

    def get_all_services(self):
        with self._lock:
            return {
                service: list(endpoints)
                for service, endpoints in self._services.items()
            }

    def print_registry(self):
        with self._lock:
            print("\n========== SERVICE REGISTRY ==========")

            if not self._services:
                print("(empty)")
            else:
                for service, endpoints in self._services.items():
                    print(f"\nService: {service}")
                    for endpoint in endpoints:
                        print(f"  -> {endpoint}")

            print("======================================\n")
