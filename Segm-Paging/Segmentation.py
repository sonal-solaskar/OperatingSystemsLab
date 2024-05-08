# SEGMENTATION 2/4/24

def segmentation(segtable):
    snum = int(input("Enter the Segment Number: "))
    d = int(input("Enter the Offset: "))
    phyadd = 0
    found = False

    for segment in segtable:
        sno, base, limit = segment
        if snum == sno:
            found = True
            if d < limit:
                phyadd = base + d
                print("Physical address is:", phyadd)
            else:
                print("Offset exceeds Limit")
            break

    if not found:
        print("Invalid Segment Number")


if __name__ == "__main__":
    segtable = []
    n = int(input("Enter the number of Segments: "))
    
    for i in range(0,n):
        ele = input(f"Enter Sno, Base and Limit for segment{i+1}: ")
        elelist = ele.split()
        elelist[0] = int(elelist[0])
        elelist[1] = int(elelist[1])
        elelist[2] = int(elelist[2])
        segtable.append(elelist)
    segmentation(segtable)