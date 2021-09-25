'''
Name: Yi Peng AndrewID: yipeng Homework: 2-5 coursenumber: 12746 
''' 
def countFamilyname():
    # receive the family name from the command
    name = input("please enter your family name")
    sum = 0
    # calculate each char of the name
    for char in name:
        num = ord(char)
    # print each char and its ascii value of the name
        print(f"The ASCII value of {char} is {num}")
        sum += num
    print(f"The sum of your family name is {sum}")
countFamilyname()