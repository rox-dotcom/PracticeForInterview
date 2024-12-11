def star(): #piramide de estrellas
    for i in range(0,5):
        for j in range(i):
            print('*', end=' ')
        print()

def table_mult(n): #te da la tabla de multiplicar de n
    for i in range(1, 11):
        res = i * n
        print(f'{i} * {n} = {res}')

def sumsAllEven(n): #Suma todos los numeros par hasta n
    sumN = 0
    for i in range(2, n + 1):
        if i % 2 == 0:
            sumN += i
    return sumN

def prime(n): #te dice si un numero es primo
    if n == 0 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True 
    
def main():
    number= int(input("enter number: "))
    #table_mult(number)
    #print(sumsAllEven(number))
    print(prime(number))


if __name__ == "__main__":
    main()