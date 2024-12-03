def theFinalProblem(target):
    n = len(target)
    initialWord = ['0']* n
    
    index = []
    count = 0
    

    for i, num in enumerate(target):
        if initialWord == target:
                break
        elif num == '1':
            initialWord[i:] = ['1'] * (n - i)
            count += 1
                  
    
    
    return(count)
    

def main():
    target = input()
    result = theFinalProblem(target)
    print(result)


if __name__ == "__main__":
    main()