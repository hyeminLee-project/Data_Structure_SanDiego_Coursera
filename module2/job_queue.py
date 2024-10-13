# python3

from collections import namedtuple
import heapq #Ensure heapq is imported

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    heap = [] # Min-heap to manage the workers based on their next free time
    #initialize the heap with all workers
    for worker in range(n_workers):
        heapq.heappush(heap, (0, worker)) # (next_free_time, worker_index)

    for job in jobs:
        next_free, worker = heapq.heappop(heap) # Get the worker who is free the soonest
        result.append(AssignedJob(worker, next_free)) # Record the job assignment
        next_free_time[worker] += job # Update when the worker will be free again
        heapq.heappush(heap, (next_free_time[worker], worker)) # Reinsert the worker into the heap
    
    return result

    # for job in jobs:
    #     next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
    #     result.append(AssignedJob(next_worker, next_free_time[next_worker]))
    #     next_free_time[next_worker] += job

    # return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
