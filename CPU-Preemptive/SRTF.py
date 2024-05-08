def srtf(plist, n):
    t = 0
    gantt = []
    completed = {} 
    burst = {} 
    
    for p in plist:
        burst[p[0]] = p[2] 
    
    while plist:
        available = []
        
        for p in plist:  
            if p[1] <= t:
                available.append(p)
                
        if available == []: 
            gantt.append("IDLE")
            t += 2
            
        else:
            available.sort(key=lambda x: x[2]) 
            process = available[0]
            t += 2 
            gantt.append(process[0])
            plist.remove(process)
            process[2] -= 2 
                         
            if process[2] == 0:  
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
    
    atat = ttat / n
    awt = twt / n
    
    print("\nProcess ID\tCompletion Time\tTurnaround Time\tWaiting Time")
    for pid, values in completed.items():
        print(f"{pid}\t\t{values[0]}\t\t{values[1]}\t\t{values[2]}")
    
    print("Avg Turn Around Time: ", atat)
    print("Avg Waiting Time: ", awt)
    print("Gantt Chart: ", gantt)           
            
            

if __name__ == "__main__":
    plist = []
    n = int(input("Enter the number of Processes: "))
    
    for i in range(0,n):
        ele = input(f"Enter PID, AT and BT for Process{i+1}: ")
        elelist = ele.split()
        elelist[1] = int(elelist[1])
        elelist[2] = int(elelist[2])
        plist.append(elelist)
    srtf(plist, n)