import random

class Client:
    def __init__(self, client_id, max_resources):
        self.client_id = client_id
        self.max_resources = max_resources
        self.allocated_resources = [0] * len(max_resources)

    def request_resources(self):
        """
        Request a random amount of resources.
        """
        request = [random.randint(0, self.max_resources[i] - self.allocated_resources[i]) for i in range(len(self.max_resources))]
        return request

    def release_resources(self):
        """
        Release a random amount of resources.
        """
        release = [random.randint(0, self.allocated_resources[i]) for i in range(len(self.max_resources))]
        return release

    def get_id(self):
        """
        Get the client ID.
        """
        return self.client_id
