

#
# def talking_numbers(num):
#     number = int(num)
#     # number = input("give me a number")
#     if number < 19:
#         if number[0] == 1:
#             print("One")
#         elif number[0] == 2:
#             print("Two")
#         elif number[0] == 3:
#             print("Three")
#         elif number[0] == 4:
#             print("Four")
#         elif number[0] == 5:
#             print("Five")
#         elif number[0] == 6:
#             print("Six")
#         elif number[0] == 7:
#             print("Seven")
#         elif number[0] == 8:
#             print("Eight")
#         elif number[0] == 9:
#             print("Nine")
#         elif number[0] == 10:
#             print("Ten")
#         elif number[0] == 11:
#             print("Eleven")
#         elif number[0] == 12:
#             print("Twelve")
#         elif number[0] == 13:
#             print("Thirteen")
#         elif number[0] == 14:
#             print("Fourteen")
#         elif number[0] == 15:
#             print("Fifteen")
#         elif number[0] ==16:
#             print("Sixteen")
#         elif number[0] == 17:
#             print("Seventeen")
#         elif number[0] == 18:
#             print("Eighteen")
#         elif number[0] == 19:
#             print("Nineteen")
#     if number > 19:
#         if number[0] == "2":
#             int1="Twenty"
#         elif number[0] == 3:
#             int1="Thirty"
#         elif number[0] == 4:
#             int1 = "Fourty"
#         elif number[0] == 5:
#             int1 = "fifty"
#         elif number[0] == 6:
#             int1 = "Sixty"
#         elif number[0] == 7:
#             int1 = "Seventy"
#         elif number[0] == 8:
#             int1 = "Eighty"
#         elif number[0] == 9:
#             int1 = "Ninty"
#             if number[1] == 1:
#                 int2 = "one"
#             elif number[1]== 2:
#                 int2 = "two"
#             elif number[1] == 3:
#                 int2 = "three"
#             elif number[1] == 4:
#                 int2 = "four"
#             elif number[1] == 5:
#                 int2 = "five"
#             elif number[1] == 6:
#                 int2 = "six"
#             elif number[1] == 7:
#                 int2 = "seven"
#             elif number[1] == 8:
#                 int2 = "eight"
#             elif number[1] == 9:
#                 int2 = "nine"
#     return int1 + int2
# talking_numbers(23)


def talking_numbers():
    num = int(input("give me a number "))
    lower = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6:"six", 7: "seven", 8: "eight", 9: "nine",
             10: "ten", 11:"eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
            17: "seventeen", 18: "eighteen", 19:"nineteen"}

    deca = {'2': "Twenty", '3': "Thirty", '4': "Fourty", "5": "Fifty", "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Nintey"}

    if (num >= 1) and (num <=19):
        print(lower[num])
    elif num > 19:
        x = str(num)
        y = int(x[1])
        print(deca[x[0]]+(lower[y]))

talking_numbers()