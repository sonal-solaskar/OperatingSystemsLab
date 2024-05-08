def calculate_difference(arr, head):
    diff = []
    for track in arr:
        diff.append(abs(track - head))
    return diff

def find_min(diff, visited):
    min_diff = float('inf') #Initially, we set min_diff to positive infinity. 
    #This ensures that any value of d in the diff list will be smaller than min_diff initially.
    min_index = -1 #Stores index of min diff
    for i, d in enumerate(diff): #i is index, d is diff
        if not visited[i] and d < min_diff:
            min_diff = d
            min_index = i
    return min_index

def sstf(arr, head, n):
    seekcount = 0
    seekseq = []
    
    if not arr:
        return
    
    visited = [False] * n #initially no element is visited
    
    while True:
        diff = calculate_difference(arr, head)
        index = find_min(diff, visited)
        
        if index == -1:
            break
        
        visited[index] = True #marks the track as visited
        seekseq.append(head) #appends the current head position
        seekcount += diff[index] #adds the seek time difference
        head = arr[index] #updates the head position to the selected track
        
    seekseq.append(head)
    
    print("Total number of seek operations: ")
    print(seekcount)
    print("Seek Sequence is: ")
    print(seekseq)
    
    time = int(input("Enter the seek time: "))
    counttime(time, seekcount)
    
def counttime(time,seekcount):
    totaltime = time*seekcount
    print("Total Seek Time is ")
    print(totaltime) 

if __name__ == "__main__":
    arr = [] 
    n = int(input("Enter the number of elements: "))
    for i in range(0, n):
        elements = int(input("Enter the element: "))
        arr.append(elements)
    head = int(input("Enter the initial head position: "))
    sstf(arr, head, n)