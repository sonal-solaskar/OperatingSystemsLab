# PRIORITY NON PREEMPTIVE CPU SCHEDULING ALGORITHM

def priority(plist):
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
            available.sort(key=lambda x: x[3])
            process = available[0]
            pid, at, bt = process[0], process[1], process[2]
            t += bt
            ct = t
            tat = ct - at
            wt = tat - bt
            plist.remove(process)
            gantt.append(pid)
            completed[pid] = [ct, tat, wt]
       
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
    priority(plist)