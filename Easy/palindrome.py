# import math

# #get digit helper function
# def get_digit(number: int, n: int) -> int:
#     return number // 10**n % 10

# #Reverse array
# # get_digit(987654321, 8)
# # 1

# # get_digit(987654321, 5)
# # 6

# #length of an int without converting to string function
# def length(number: int) -> int:
#     if number > 0:
#         digits = int(math.log10(number))+1
#     elif number == 0:
#         digits = 1
#     else:
#         digits = int(math.log10(-number))+2
#     return digits


# def palindrome(x: int):
#     if x < 0:
#         return False
#     else:
#         A = []
#         B = []

#         #To left
#         for i in range(0, (length(x) // 2)):
#             A.append(get_digit(x, i))
        
#         #To right
#         if length(x) % 2 == 0:
#             for j in range(length(x)-1, length(x) // 2-1, -1):
#                 B.append(get_digit(x, j))
#         else:
#             for j in range(length(x)-1, length(x) // 2, -1):
#                 B.append(get_digit(x, j))

#         if A == B:
#             return True
#         else:
#             return False

def palindrome(x: int) -> bool:
    if x < 0:
        return False

    div = 1
    while x >= 10 * div:
        div *= 10

    while x:
        if x // div != x % 10:
            return False

        x = (x % div) // 10
        div = div / 100
    return True

print(palindrome(121))