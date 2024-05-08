def pageFaults(pages, n, capacity):
    frames = []
    hits = 0
    faults = 0
    result = ''
    output = "Reference   Frames     Page Hit/Faults\n"

    for reference in pages:
        if reference in frames:
            result = 'H'
            hits += 1
        else:
            result = 'F'
            faults += 1
            if len(frames) < capacity:
                frames.append(reference)
            else:
                frames.pop(0)
                frames.append(reference)
        output += f"{reference:<12}{' '.join(map(str, frames)):<12}{result}\n"

    hit_ratio = hits / n
    fault_ratio = faults / n

    output += f"Total Page Hits: {hits}\n"
    output += f"Total Page Faults: {faults}\n"
    output += f"Hit Ratio: {hit_ratio}\n"
    output += f"Fault Ratio: {fault_ratio}\n"

    print(output)

if __name__ == '__main__':
    pages = []
    capacity = int(input("Enter the frame size: "))
    n = int(input("Enter the number of pages: "))
    print("Enter the page references:")
    pages = list(map(int, input().split()))
    pageFaults(pages, n, capacity)
