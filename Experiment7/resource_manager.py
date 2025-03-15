from bankers_algorithm import BankersAlgorithm

class ResourceManager:
    def __init__(self, available, maximum, allocation):
        self.bankers_algorithm = BankersAlgorithm(available, maximum, allocation)

    def request_resources(self, request, process_id):
        """
        Request resources for a process using the Banker's Algorithm.
        """
        return self.bankers_algorithm.request_resources(request, process_id)

    def release_resources(self, release, process_id):
        """
        Release resources held by a process.
        """
        self.bankers_algorithm.release_resources(release, process_id)

    def get_available_resources(self):
        """
        Get the available resources.
        """
        return self.bankers_algorithm.available
