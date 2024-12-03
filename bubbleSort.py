def bubble_sort(list):
    unsorted_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True 
        for i in range(unsorted_index):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
        unsorted_index = unsorted_index - 1
    

def main():
    lista = [65,55,45,5,25,10,15]
    bubble_sort(lista)
    print(lista)

if __name__ == "__main__":
    main()