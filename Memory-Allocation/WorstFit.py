#WORST FIT DYNAMIC MEMORY ALLOCATION ALGORITHM
#LARGE INTERNAL FRAGMENTATION BUT SLOW

def worstFit(blockSize, m, processSize, n): 
    allocation = [-1] * n 
    
    for i in range(n): 
        wstIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                if wstIdx == -1 or blockSize[wstIdx] < blockSize[j]: 
                    wstIdx = j 

        if wstIdx != -1: 
            allocation[i] = wstIdx 
            blockSize[wstIdx] -= processSize[i] 

    print("\nProcess No.\tProcess Size\tBlock no.\tRemaining Size")
    for i in range(n):
        print(f" {i + 1}\t\t{processSize[i]}\t\t", end="")
        if allocation[i] != -1:
            print(f"{allocation[i] + 1}\t\t{blockSize[allocation[i]]}")
        else:
            print("Not Allocated")
        print() 

if __name__ == '__main__': 
    m = int(input("Enter the number of memory blocks: "))
    blockSize = []
    for i in range(m):
        size = int(input(f"Enter the size of memory block {i+1}: "))
        blockSize.append(size)

    n = int(input("Enter the number of processes: "))
    processSize = []
    for i in range(n):
        size = int(input(f"Enter the size of process {i+1}: "))
        processSize.append(size)

    worstFit(blockSize, m, processSize, n)