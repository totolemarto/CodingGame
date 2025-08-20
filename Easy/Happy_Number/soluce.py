def is_happy(x : int) -> str:
    need_to_continue : bool = True
    prev : dict[int, int] = {}
    prev[x] = 1
    while x != 1 and need_to_continue:
        number_str : str = str(x)
        x = sum(int(figure) ** 2 for figure in number_str)
        need_to_continue = x not in prev.keys() 
        prev[x] = 1
    return ":)" if x == 1 else ":("

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        x = int(input())
        print(x, is_happy(x))
