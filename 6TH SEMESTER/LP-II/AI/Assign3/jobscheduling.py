"""
Assignment-A3.IV (Job Scheduling)

Problem Statement: Implement Greedy search algorithm for any of the following application:
  IV. Job Scheduling Problem
"""

def job_scheduling():
    jobs = []
    total = int(input("Total jobs to add:\t"))

    # Take input for jobs
    print("\n", "-"*10, "JOBS", "-"*10, "\n")
    for i in range(total):
        print(f"JOB {i+1} ->")
        job_id = int(input(f"ID for job {i+1}:\t\t"))
        deadline = int(input(f"Deadline for job {i+1}:\t"))
        profit = int(input(f"Profit for job {i+1}:\t"))
        jobs.append((job_id, deadline, profit)) # Index 0 for job_id; Index 1 for deadline; Index 2 for profit
    print(f"\nAdded {total} jobs.")
    print("-"*27, "\n")

    # Initialize
    jobs.sort(key=lambda x: x[2], reverse=True) # Sort jobs by profit; Using index 2 to access profit
    max_deadline = max(job[1] for job in jobs) # Highest deadline; Using index 1 to access deadline
    slots = [0] * (max_deadline + 1)
    total_profit = 0

    # Scheduling jobs using greedy strategy
    for job in jobs:
        for i in range(job[1], 0, -1):
            if slots[i] == 0:
                slots[i] = job[0]
                total_profit += job[2]
                break

    # Print scheduled jobs
    print("Scheduled Jobs:", end=" ")
    for i in range(1, len(slots)):
        if slots[i] != 0:
            print(slots[i], end=" ")

    print(f"\nTotal Profit: {total_profit}\n")

job_scheduling()
