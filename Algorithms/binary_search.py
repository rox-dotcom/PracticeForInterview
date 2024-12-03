#Binary Search
def binary_Search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1
        else:
            None
            

def main():
    lista = list(range(1, 50))
    result = binary_Search(lista, 10)
    if result is not None:
        print(f"Target found at {result}")
    else:
        print("Target not in list")



if __name__ == '__main__':
    main()
           
