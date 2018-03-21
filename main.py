#                                                           ©Jonathan Webber
#This is a simple program that checks to see if a user-inputted string is a palindrome.

#user input for a string
print('Please enter the string you would like check for palindrome-ism: ')
userStr = input()

#funtion to reverse a string
def revStr(str):
    #temporary string
    tempStr = ''

    #if the user input has nothing in it
    if(len(str)==0):
        return ''

    #loop to put the end of the string into the beginning of tempStr
    for i in range(0, len(str)):
        tempStr += str[-1-i]

    #return the string
    return tempStr

#funtion to check if two strings are palindromes
def isPalindrome(str):
    if(str == revStr(str)):
        return True
    else:
        return False

#print out the string
if(isPalindrome(userStr)):
    print('Your string is a palindrome.')
else:
    print('Your string is not a palindrome.')