#reverse a given string and check palindrome
def palindrome(s):
    b=s[::-1]
    print(b)
    if s==b:
        return "it is a Palindrome"
    return "it is not a Palindrome"
s=input()
print(palindrome(s))
