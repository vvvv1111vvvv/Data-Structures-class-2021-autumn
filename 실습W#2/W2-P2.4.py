def draw_tree(row,left,right):
    for j in range(0,2**row):
        for i in range (0,left):
            print(" - ", end='')
        print(" X ", end='')
        for i in range (0,right):
            print(" - ", end='')
    print("\n")
    if left==1:
        return
    draw_tree(row+1,(left+1)//2,(right-1)//2)
draw_tree(row=0,left= 31, right= 32)