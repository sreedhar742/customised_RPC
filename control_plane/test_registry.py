from registry import ServiceRegistry
registry = ServiceRegistry()

registry.add_endpoint("backend", "172.18.0.5:8000")
registry.add_endpoint("backend", "172.18.0.6:8000")
registry.add_endpoint("auth", "172.18.0.10:9000")

registry.print_registry()

registry.remove_endpoint("backend", "172.18.0.5:8000")

registry.print_registry()
