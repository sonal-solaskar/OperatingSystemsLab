# ROUND ROBIN PREEMPTIVE CPU SCHEDULING ALGORITHM

def robin(plist, qt, n):
    t = 0
    gantt = []
    completed = {} #track of completed processes
    burst = {} #track of pid and bt
    
    for p in plist:
        burst[p[0]] = p[2] #Key value is pid ie pid : bt
    
    plist.sort(key=lambda x: x[1]) #sort by at

    while plist: 
        available = []
        
        for p in plist:  #check available process
            if p[1] <= t:
                available.append(p)
                
        if available == []: #no process available at time t
            gantt.append("IDLE")
            t += 1 #inc by 1 since preemptive
            
        else:
            
            process = available[0]
            pid = process[0]
            gantt.append(pid) #add to chart
            #remove process
            plist.remove(process)
            remburst = process[2]
            #checking boundary condition
            if remburst <= qt: 
                t += remburst
                completed[pid] = t
                at = process[1]
                bt = burst[pid]
                ct = t
                tat = ct - at
                wt = tat - bt
                completed[pid] = [ct, tat, wt]
                
            else:
                t += qt
                process[2] -= qt
                plist.append(process)
    ttat = 0
    twt = 0
    for pid in completed:
        ttat += completed[pid][1]
        twt += completed[pid][2]
    
    atat = ttat / n
    awt = twt / n
    
    print("Avg Turn Around Time: ", atat)
    print("Avg Waiting Time: ", awt)            
    print("Gantt Chart: ", gantt)
    print("Completed: ", completed) 

if __name__ == "__main__":
    plist = []
    n = int(input("Enter the number of Processes: "))
    qt = int(input("Enter Time Quantum: "))
    for i in range(0,n):
        ele = input(f"Enter PID, AT and BT for Process{i+1}: ")
        elelist = ele.split()
        elelist[1] = int(elelist[1])
        elelist[2] = int(elelist[2])
        plist.append(elelist)
    robin(plist, qt, n)