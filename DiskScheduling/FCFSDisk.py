# FCFS Disk Scheduling algorithm
def fcfs(arr, head, n):
    seekcount = 0
    distance = 0
    cur_track = 0
    
    for i in range(n):
        cur_track = arr[i]
        distance = abs(cur_track - head)        
        seekcount += distance
        head = cur_track
    
    print("Seek Distance is ", end="")
    print(seekcount)
    
    print("Seek Sequence is ", end="")
    for i in range(n):
        print(arr[i], end=" ")
    
    time = int(input("\nEnter the seek time: "))
    counttime(time, seekcount)



def counttime(time,seekcount):
    totaltime = time*seekcount
    print("Total Seek Time is ")
    print(totaltime)
    

if __name__ == "__main__":
   arr = [] 
   n = int(input("Enter the number of tracks: "))
   for i in range(0,n):
       elements = int(input("Enter the tracks: "))
       arr.append(elements)
   head = int(input("Enter the initial head position: "))
fcfs(arr, head, n)     
