def scan_algorithm(arr, head, direction, total_tracks):
    seek_count = 0
    seek_sequence = []

    # Sort the requests according to the current head position
    arr.sort()

    # Set up a set to keep track of serviced requests
    serviced = set()

    while True:
        if direction == "right":
            for track in range(head, total_tracks):  # Adjusted loop condition
                if track in arr and track not in serviced:
                    seek_sequence.append(track)
                    seek_count += abs(track - head)
                    head = track
                    serviced.add(track)
            # Add the extreme point of the chosen direction to the seek sequence and count
            seek_sequence.append(total_tracks - 1)
            seek_count += abs(total_tracks - 1 - head)
            head = total_tracks - 1
            #Calculate for left after right
            for track in range(head, -1, -1):
                if track in arr and track not in serviced:
                    seek_sequence.append(track)
                    seek_count += abs(track - head)
                    head = track
                    serviced.add(track)
                    
                    
        else:
            for track in range(head, -1, -1):
                if track in arr and track not in serviced:
                    seek_sequence.append(track)
                    seek_count += abs(track - head)
                    head = track
                    serviced.add(track)
            # Add the extreme point of the chosen direction to the seek sequence and count
            seek_sequence.append(0)
            seek_count += abs(0 - head)
            head = 0
            #Calculate for right after left
            for track in range(head, total_tracks):  # Adjusted loop condition
                if track in arr and track not in serviced:
                    seek_sequence.append(track)
                    seek_count += abs(track - head)
                    head = track
                    serviced.add(track)
                    
        # If all requests have been serviced, break the loop
        if len(serviced) == len(arr):
            break

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
    scan_algorithm(arr, head, direction, total_tracks)
