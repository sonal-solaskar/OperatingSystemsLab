# PAGING 2/4/24
def paging(ptable,size):
    pnum = int(input("Enter the Page Number: "))
    d = int(input("Enter the Offset: "))
    found = False

    for page in ptable:
        pno, fno = page
        if pnum == pno:
            found = True
            if d < size:
                print(f"Physical address is: {fno}{d}")
            else:
                print("Offset exceeds Page Size")
            break

    if not found:
        print("Invalid Page Number") 

if __name__ == "__main__":
    ptable = []
    n = int(input("Enter the number of Pages: "))
    size = int(input("Enter the size of Pages: "))
    
    for i in range(0,n):
        ele = input(f"Enter PageNo. and FrameNo. for page{i+1}: ")
        elelist = ele.split()
        elelist[0] = int(elelist[0])
        elelist[1] = int(elelist[1])
        ptable.append(elelist)
    paging(ptable,size)