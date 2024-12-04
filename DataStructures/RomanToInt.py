"""___HASHMAP___"""
#NOT MY SOLUTION... to improve in LeetCode
def romanToInt(s):
    r= {'I':1, #Hash map/ dictionary
        'V':5, 
        'X':10, 
        'L':50, 
        'C':100,
        'D':500,
        'M':1000
        } 
    integer = 0 #the sum of the num
    pre = s[-1] #this is always the last number in our string (ex. if given this 'IV', pre would be 'V') 
    for i in range(len(s)-1,-1,-1): #Moves in reverse order, 
                                    #it starts at the end of the list with len(s)-1 [for exapmple: len(s)=5 - 1= 4 the last element of the list] 
                                    #the loop stops before -1, to iterate until the first element (0)
                                    #it takes -1 steps each time, so backward iteration for the loop
        if r[s[i]] <r[pre]: 
            integer -=r[s[i]] #If the current value is less than pre, we rest the value
        else:
            integer +=r[s[i]] #else it is the same or bigger, so we add it to our result
        pre = s[i] #So that if we have a rest in between a big number it can be answered correctly[ex. 'XCIV' this is 94 in roman Numbers, so we need to rest the X from C, and the I from V]
                    # refreshes to be the character before the new char evaluated  
    return integer

def main():
    print(romanToInt('XCIV'))

main()