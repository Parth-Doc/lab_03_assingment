class Process:
    def __init__(self, pid, process, start_time, priority):
        self.pid = pid
        self.process = process
        self.start_time = start_time
        self.priority = priority

    def __repr__(self):
        return f"Process({self.pid}, {self.process}, {self.start_time}, {self.priority})"


def custom_priority_order(priority):
    order = {"Low": 1, "MID": 2, "High": 3}
    return order.get(priority, 0)


def print_table(processes):
    print("P_ID\tProcess\tStart Time (ms)\tPriority")
    for process in processes:
        print("%s\t%s\t%s\t%s" % (process.pid, process.process, process.start_time, process.priority))


def main():
    processes = [
        Process("P1", "VSCode", 100, "MID"),
        Process("P23", "Eclipse", 234, "MID"),
        Process("P93", "Chrome", 189, "High"),
        Process("P42", "JDK", 9, "High"),
        Process("P9", "CMD", 7, "Low"),
        Process("P87", "NotePad", 23, "Low")
    ]

    print("Choose a sorting parameter:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time (ms)")
    print("3. Sort by Priority")

    choice = int(input())

    if choice == 1:
        processes.sort(key=lambda x: int(x.pid[1:]))
    elif choice == 2:
        processes.sort(key=lambda x: x.start_time)
    elif choice == 3:
        processes.sort(key=lambda x: (custom_priority_order(x.priority), x.priority))
    else:
        print("Invalid choice.")
        sys.exit(1)

    print_table(processes)


if __name__ == "__main__":
    main()
