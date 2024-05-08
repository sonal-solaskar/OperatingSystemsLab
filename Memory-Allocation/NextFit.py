def NextFit(blockSize, m, processSize, n):
    allocation = [-1] * n

    j = 0
    t = m - 1
    for i in range(n):
        while j < m:
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]

                t = (j - 1) % m
                break
            if t == j:
                t = (j - 1) % m
                break

            j = (j + 1) % m

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
        size = int(input(f"Enter the size of memory block {i + 1}: "))
        blockSize.append(size)

    n = int(input("Enter the number of processes: "))
    processSize = []
    for i in range(n):
        size = int(input(f"Enter the size of process {i + 1}: "))
        processSize.append(size)

    NextFit(blockSize, m, processSize, n)
