def c_scan_algorithm(arr, head, direction, total_tracks):
    seek_count = 0
    seek_sequence = []

    # Sort the requests according to the current head position
    arr.sort()

    # Set up a set to keep track of serviced requests
    serviced = set()

    # Determine the starting point based on the direction
    start_track = 0 if direction == "right" else total_tracks - 1

    # Handle requests in one direction
    while True:
        direction_changed = False  # Flag to track direction change
        for track in range(head, total_tracks) if direction == "right" else range(head, -1, -1):
            if track in arr and track not in serviced:
                seek_sequence.append(track)
                seek_count += abs(track - head)
                head = track
                serviced.add(track)
                direction_changed = True  # Request serviced, so can change direction

        # If direction changed, calculate the seek count till the end of the disk
        if direction_changed:
            if direction == "right":
                seek_sequence.append(total_tracks - 1)
                seek_count += abs(total_tracks - 1 - head)
                head = total_tracks - 1
            else:
                seek_sequence.append(0)
                seek_count += abs(0 - head)
                head = 0

        # If all requests have been serviced, break the loop
        if len(serviced) == len(arr):
            break

        # Change direction after servicing all requests in the current direction
        direction = "left" if direction == "right" else "right"

    print("Total number of seek operations:")
    print(seek_count)
    print("Seek Sequence is:")
    print(seek_sequence)

    time = int(input("Enter the seek time: "))
    count_time(time, seek_count)


def count_time(time, seek_count):
    total_time = time * seek_count
    print("Total Seek Time is:")
    print(total_time)


if __name__ == "__main__":
    arr = []
    n = int(input("Enter the number of tracks: "))
    for i in range(n):
        element = int(input("Enter the track number: "))
        arr.append(element)
    head = int(input("Enter the initial head position: "))
    direction = input("Enter the initial direction (left/right): ").lower()
    total_tracks = int(input("Enter the total number of tracks on the disk: "))
    c_scan_algorithm(arr, head, direction, total_tracks)
