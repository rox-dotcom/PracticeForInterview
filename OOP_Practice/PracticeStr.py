def reverseStr(word):
    newWord = []
    for i in range (1,len(word)+1):
        newWord.append(word[-i])
    return ''.join(newWord)
    # or just do this 
    #return word[::-1]

def palindrome(word):
    word= word.lower().replace(' ', '')
    for i in range(len(word)):
        if word[i] != word[-(i+1)]:
            return False
    return True
    #or return word == word[::-1]
        
# Write a program to count the number of 
# vowels in a user-entered string.
def countVocals(word): 
    word = word.lower()
    vowels = {'a', 'e', 'i','o','u'}
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count 

def main():
    #print(reverseStr('Lona'))
    #print(palindrome('Anita lava la tina'))
    print(countVocals('HEllo Friend'))


if __name__ == "__main__":
    main()