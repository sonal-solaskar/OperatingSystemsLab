def clook_algorithm(arr, head, direction, total_tracks):
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
            # Modified to handle requests beyond the head position
            for track in range(0, head):  # Only consider tracks before head
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
            # Modified to handle requests beyond the head position
            for track in range(total_tracks - 1, head, -1):  # Only consider tracks after head
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
    clook_algorithm(arr, head, direction, total_tracks)
