# FCFS CPU SCHEDULING ALGORITHM
def fcfs(plist,n):
    t = 0
    gantt = []
    completed = {}
    plist.sort(key=lambda x: x[1]) #sort by at 
    while plist:
        process = plist.pop(0) #get the first process after sorting
        pid, at, bt = process[0], process[1], process[2] #assign values
        if t < at: #no process has arrived at time t
            gantt.append("IDLE") 
            t = at #since next process arrives at at directly, assign t = at
        gantt.append(pid) 
        t += bt
        ct = t
        tat = ct - at
        wt = tat - bt
        completed[pid] = [ct, tat, wt] #key value is pid
    ttat = 0
    twt = 0
    for pid in completed:
        ttat += completed[pid][1]
        twt += completed[pid][2]
    
    atat = ttat / n
    awt = twt / n
    
    print("Avg Turn Around Time: ", atat)
    print("Avg Waiting Time: ", awt)
    print("Gantt Chart: ",gantt)
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
    fcfs(plist,n)