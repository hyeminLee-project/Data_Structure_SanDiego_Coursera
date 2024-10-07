from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()  # Using deque to manage processing times efficiently

    def process(self, request):
        # Remove all finished packets from the buffer
        while self.finish_time and self.finish_time[0][0] <= request.arrived_at:
            self.finish_time.popleft()

        # Check if the buffer is full
        if len(self.finish_time) >= self.size:
            return Response(True, -1)  # Packet is dropped

        # Determine when the packet can start processing
        if not self.finish_time:
            # If the buffer is empty, we can start processing immediately
            start_time = request.arrived_at
        else:
            # Start processing after the last packet finishes
            start_time = max(request.arrived_at, self.finish_time[-1][0])

        # Calculate finish time for the current packet
        finish_time = start_time + request.time_to_process
        
        # Store the finish time in the deque
        self.finish_time.append((finish_time, request))

        return Response(False, start_time)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses

def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)

if __name__ == "__main__":
    main()
