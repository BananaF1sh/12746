'''
Name: Yi Peng AndrewID: yipeng Homework: 2-3 coursenumber: 12746 
''' 
def sayHello():
    #receive the arguments from the command
    name = input("please enter your name\n")
    age = int(input("please enter your age\n"))
    
    print(f"Hello! {name},I am Yi Peng!\n")
    if(age > 23):
        print("You are older than me!")
    elif(age < 23):
        print("You are younger than me!")
    else:
        print("We are the same age!")


sayHello()