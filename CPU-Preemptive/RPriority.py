def priority(plist,n):
    t = 0
    gantt = []
    completed = {} # track of completed processes
    burst = {} # track of pid and bt
    
    for p in plist:
        burst[p[0]] = p[2] # Key value is pid ie pid : bt
    
    while plist:
        available = []
        
        for p in plist:  # check available process
            if p[1] <= t:
                available.append(p)
                
        if available == []: # no process available at time t
            gantt.append("IDLE")
            t += 1 # inc by 1 since preemptive
            
        else:
            available.sort(key=lambda x: x[3], reverse=True) # sort by priority (higher priority first)
            process = available[0]
            gantt.append(process[0])
            t += 1 # inc by 1 since preemptive
            plist.remove(process)
            process[2] -= 1 # dec bt by 1 since preemptive
            
            if process[2] == 0:  # completed process ie bt = 0
                pid = process[0]
                completed[pid] = t
                at = process[1]
                bt = burst[pid]
                ct = t
                tat = ct - at
                wt = tat - bt
                completed[pid] = [ct, tat, wt]
                
            else:
                plist.append(process)
                
    ttat = 0
    twt = 0
    for pid in completed:
        ttat += completed[pid][1]
        twt += completed[pid][2]
    
    atat = (ttat / n)
    awt = (twt / n)
    
    print("Avg Turn Around Time: ", atat)
    print("Avg Waiting Time: ", awt)
    print("Gantt Chart: ",gantt)
    print("Completed: ",completed)                    

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
