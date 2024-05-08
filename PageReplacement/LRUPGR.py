def simulate_lru(pages, n, capacity):
    frames = []
    hits = 0
    faults = 0
    page_last_used = {}  # Dictionary to track the last usage of each page
    output = "Reference   Frames     Page Hit/Faults\n"
    for i, reference in enumerate(pages):
        if reference in frames:
            result = 'H'
            hits += 1
            page_last_used[reference] = i
        else:
            result = 'F'
            faults += 1
            if len(frames) < capacity:
                frames.append(reference)
                page_last_used[reference] = i
            else:
                # Find the least recently used page in frames
                lru_page = min(frames, key=lambda x: page_last_used.get(x, float('inf')))
                # Replace the least recently used page with the new page
                frames[frames.index(lru_page)] = reference
                # Update the last usage of the new page
                page_last_used[reference] = i
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
    simulate_lru(pages, n, capacity)
