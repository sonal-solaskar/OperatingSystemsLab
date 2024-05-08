# PRIORITY NON PREEMPTIVE CPU SCHEDULING ALGORITHM

def priority(plist,n):
    t = 0
    gantt = []
    completed = {}
    while plist:
        available = []
        for p in plist:
            if p[1] <= t:
                available.append(p)
        
        if available == []:
            gantt.append("IDLE")
            t += 1
            
        else:
            available.sort(key=lambda x: x[3]) #sort by priority
            process = available[0]
            pid, at, bt = process[0], process[1], process[2]
            t += bt
            ct = t
            tat = ct - at
            wt = tat - bt
            plist.remove(process)
            gantt.append(pid)
            completed[pid] = [ct, tat, wt]
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
    n = int(input("Enter the number of Processes: "))
    
    for i in range(0,n):
        ele = input(f"Enter PID, AT, BT and Priority for Process{i+1}: ")
        elelist = ele.split()
        elelist[1] = int(elelist[1])
        elelist[2] = int(elelist[2])
        elelist[3] = int(elelist[3])
        plist.append(elelist)
    priority(plist,n)