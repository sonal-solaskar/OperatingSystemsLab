# SJF CPU SCHEDULING ALGORITHM
def sjf(plist,n):
    t = 0
    gantt = []
    completed = {}
    
    while plist:
        available = []
        
        for p in plist: 
            if p[1] <= t: #process is available at at or not
                available.append(p)
        
        if available == []:
            gantt.append("IDLE")
            t += 1
        else:
            available.sort(key= lambda x: x[2]) #sort by bt 
            process = available[0] #first available process
            pid, at, bt = process[0], process[1], process[2]
            t += bt
            ct = t
            tat = ct - at
            wt = tat - bt
            gantt.append(pid)
            plist.remove(process) #remove process after completed
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
        ele = input(f"Enter PID, AT and BT for Process{i+1}: ")
        elelist = ele.split()
        elelist[1] = int(elelist[1])
        elelist[2] = int(elelist[2])
        plist.append(elelist)
    sjf(plist,n)
