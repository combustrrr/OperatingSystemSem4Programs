class BankersAlgorithm:
    def __init__(self, available, maximum, allocation):
        self.available = available
        self.maximum = maximum
        self.allocation = allocation
        self.need = self.calculate_need()
        self.num_processes = len(allocation)
        self.num_resources = len(available)

    def calculate_need(self):
        need = []
        for i in range(len(self.maximum)):
            need.append([self.maximum[i][j] - self.allocation[i][j] for j in range(len(self.available))])
        return need

    def is_safe(self, request, process_id):
        """
        Check if the system is in a safe state after allocating 'request' to process 'process_id'.
        """
        temp_available = self.available[:]
        temp_allocation = [row[:] for row in self.allocation]
        temp_need = [row[:] for row in self.need]

        # Simulate the allocation
        for i in range(self.num_resources):
            temp_available[i] -= request[i]
            temp_allocation[process_id][i] += request[i]
            temp_need[process_id][i] -= request[i]

        # Check if the new state is safe
        work = temp_available[:]
        finish = [False] * self.num_processes

        while True:
            allocated = False
            for i in range(self.num_processes):
                if not finish[i] and all(temp_need[i][j] <= work[j] for j in range(self.num_resources)):
                    work = [work[j] + temp_allocation[i][j] for j in range(self.num_resources)]
                    finish[i] = True
                    allocated = True
            if not allocated:
                break

        return all(finish)

    def request_resources(self, request, process_id):
        """
        Request resources for a process.
        """
        # Check if request exceeds need
        for i in range(self.num_resources):
            if request[i] > self.need[process_id][i]:
                return False  # Request exceeds need

        # Check if request exceeds available
        for i in range(self.num_resources):
            if request[i] > self.available[i]:
                return False  # Request exceeds available

        # Check if the system is in a safe state after the request
        if self.is_safe(request, process_id):
            # Simulate the allocation
            for i in range(self.num_resources):
                self.available[i] -= request[i]
                self.allocation[process_id][i] += request[i]
                self.need[process_id][i] -= request[i]
            return True  # Request granted
        else:
            return False  # Request denied

    def release_resources(self, release, process_id):
        """
        Release resources held by a process.
        """
        # Release the resources
        for i in range(self.num_resources):
            self.available[i] += release[i]
            self.allocation[process_id][i] -= release[i]
            self.need[process_id][i] += release[i]
