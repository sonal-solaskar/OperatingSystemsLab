# FCFS CPU SCHEDULING ALGORITHM
def fcfs(plist):
    t = 0
    gantt = []
    completed = {}
    plist.sort(key=lambda x: x[1])
    while plist:
        process = plist.pop(0)
        pid, at, bt = process[0], process[1], process[2]
        if t < at:
            gantt.append("IDLE")
            t = at
        gantt.append(pid)
        t += bt
        ct = t
        tat = ct - at
        wt = tat - bt
        completed[pid] = [ct, tat, wt]
    print(gantt)
    print(completed)

if __name__ == "__main__":
    plist = []
    n = int(input("Enter the number of processes: "))
    for i in range(n):
        ele = input(f"Enter the ProcessID, Arrival and Burst time at Process {i+1}: ")
        elelist = ele.split()
        elelist[1] = int(elelist[1])
        elelist[2] = int(elelist[2])
        plist.append(elelist)
    fcfs(plist)