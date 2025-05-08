def round_robin_scheduling(tasks, time_quantum):
    """
    Simulates Round Robin scheduling on given tasks.
    Each task is a dictionary with keys: name, arrival_time, burst_time.
    """
    time = 0
    queue = tasks[:]
    waiting_times = {}
    turnaround_times = {}
    remaining_bt = {task['name']: task['burst_time'] for task in tasks}

    print("\n🔄 Round Robin Task Execution Order:")
    while queue:
        task = queue.pop(0)
        name = task['name']
        arrival = task['arrival_time']
        bt_left = remaining_bt[name]

        if bt_left > 0 and arrival <= time:
            exec_time = min(time_quantum, bt_left)
            print(f"🕒 Time {time} -> {time + exec_time}: {name} running ({exec_time} units)")

            time += exec_time
            remaining_bt[name] -= exec_time

            if remaining_bt[name] == 0:
                turnaround_times[name] = time - arrival
                waiting_times[name] = turnaround_times[name] - task['burst_time']
            else:
                queue.append(task)
        elif arrival > time:
            time += 1
            queue.append(task)

    return waiting_times, turnaround_times


def main():
    print("📋 Task Scheduler Management System (Round Robin)\n")
    try:
        n = int(input("Enter number of tasks: "))
        time_quantum = int(input("Enter Time Quantum: "))
        tasks = []

        for i in range(n):
            name = input(f"\nEnter name of Task {i+1}: ")
            arrival = int(input("Arrival Time: "))
            burst = int(input("Burst Time: "))
            tasks.append({"name": name, "arrival_time": arrival, "burst_time": burst})

        wt, tat = round_robin_scheduling(tasks, time_quantum)

        print("\n📊 Task Summary:")
        print(f"{'Task':<10}{'Waiting Time':<15}{'Turnaround Time'}")
        for name in wt:
            print(f"{name:<10}{wt[name]:<15}{tat[name]}")

        avg_wt = sum(wt.values()) / n
        avg_tat = sum(tat.values()) / n
        print(f"\n📈 Average Waiting Time: {avg_wt:.2f}")
        print(f"📈 Average Turnaround Time: {avg_tat:.2f}")

    except ValueError:
        print("⚠️ Invalid input! Please enter only numeric values where required.")

if __name__ == "__main__":
    main()
