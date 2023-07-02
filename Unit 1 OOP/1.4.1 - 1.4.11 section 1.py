# 1.4.1 Problem 1
a, b = (2, 3)
print(a + b) #returns 5

a, b = [2, 3]
print(a + b) # returns 5

[a, b] = (2, 3)
print(a + b) # returns 5

(a, b) = [2, 3]
print(a + b) # returns 5

# (a, b) = (2, 3, 4)
# print(a + b) # returns error, too many values to unpack

# (a, b) = (2)
# print(a + b) # returns error, too little to unpack

# (a, (b, c)) = (2, 3, 4)
# print(a + b + c) # returns error, too many values to unpack

# 1.4.3
def evenSquares(nums):
    evenSquares = [num ** 2 for num in nums if num % 2 == 0]
    print(evenSquares)
    return evenSquares

evenSquares([1, 2, 3, 4, 5, 6])

def sumAbsProd(list1, list2):
    sumAbsProd = sum([abs(x * y) for x in list1 for y in list2])
    print(sumAbsProd)
    return sumAbsProd

sumAbsProd([2, -3], [4, -5])

# need more list comprehension practice

# 1.4.7 optional
def isPalindrome(string):
    forward_i = 0
    backwards_i = -1
    for i in string:
        if string[forward_i] == string[backwards_i]:
            forward_i += 1
            backwards_i -= 1
        
        else:
            return False

    return True

isPalindrome("racecar")

# 1.4.8 substring optional
def isSubstring(str1, str2):
    

