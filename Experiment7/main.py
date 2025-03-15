import sys
import os
sys.path.append(os.path.dirname(__file__))

import random
from resource_manager import ResourceManager
from client import Client

def main():
    # Define the resources
    num_resources = 3
    available = [10, 5, 7]

    # Define the clients
    num_clients = 5
    maximum = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]  # Max resources for each client
    allocation = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Currently allocated resources

    # Initialize the resource manager
    resource_manager = ResourceManager(available, maximum, allocation)

    # Initialize the clients
    clients = [Client(i, maximum[i]) for i in range(num_clients)]

    # Simulate resource allocation
    for _ in range(10):
        client_id = random.randint(0, num_clients - 1)
        client = clients[client_id]

        # Request resources
        request = client.request_resources()
        print(f"Client {client_id} requesting: {request}")
        if resource_manager.request_resources(request, client_id):
            print(f"Request granted for client {client_id}")
            for i in range(num_resources):
                client.allocated_resources[i] += request[i]
        else:
            print(f"Request denied for client {client_id}")

        # Release resources
        release = client.release_resources()
        print(f"Client {client_id} releasing: {release}")
        resource_manager.release_resources(release, client_id)
        for i in range(num_resources):
            client.allocated_resources[i] -= release[i]

        print(f"Available resources: {resource_manager.get_available_resources()}")
        print("-" * 30)

if __name__ == "__main__":
    main()
