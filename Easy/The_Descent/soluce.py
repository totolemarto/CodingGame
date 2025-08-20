heights : list[int] = [-1]*8
while True:
    for i in range(8):
        mountain_h : int = int(input())  
        heights[i] = mountain_h
    x : int = (heights.index(max(heights)))
    print(x)
