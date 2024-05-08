#BEST FIT DYNAMIC MEMORY ALLOCATION ALGORITHM
#MEMORY EFFICIENT BUT SLOW

def best_fit(blockSize, m, processSize, n):
    allocation = [-1] * n  
    
    for i in range(n):
        bestIdx = -1  
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1 or blockSize[bestIdx] > blockSize[j]: #if current block j is smaller then assign bestIdx to j
                    bestIdx = j

        if bestIdx != -1: #block found
            allocation[i] = bestIdx #allocation
            blockSize[bestIdx] -= processSize[i] #updation

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
        
    best_fit(blockSize, m, processSize, n)    
