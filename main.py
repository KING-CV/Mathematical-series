'''
Name    :   Chirag Singh
Uid     :   U90684694
About   :   This program allows the user to choose from many number series. This program allows the user to give a number.
and the number gives gives the n'th term from the series.
          the user can also select on which kind ofseries he wants from the menu
'''

def fib():#use return
    quit = False
    n_list = int(input("Enter the number of values from list(>=3):"))
    list = []
    num = int()
    while n_list<3:
        n_list = int(input("Invalid entry. Re-enter the number of values from list(>=3):"))
    for i in range(1,n_list+1):
        if i ==1 or i ==2:
            num = 1
            list.append(num)
        else:
            num = list[-1]+list[-2]
            list.append(num)
    print(f"Here's the list containing first {n_list} numbers of Fibonacci series{list}")


def catalan():
    list = [1.0]
    import math
    n_list = int(input("Enter the number of values from list(>=3):"))
    while n_list<3:
        n_list = int(input("Invalid entry. Re-enter the number of values from list(>=3):"))
    for i in range(1,n_list+1):
        num = math.factorial(2*i)
        num= num/math.factorial(i+1)
        num = num/math.factorial(i)
        list.append(num)
    list.pop()
    print(f"Here's the list containing first {n_list} numbers of Catalan series{list}")

def lazy():

    list = [1.0]
    n_list = int(input("Enter the number of values from list(>=3):"))
    while n_list < 3:
        n_list = int(input("Invalid entry. Re-enter the number of values from list(>=3):"))
    for i in range(1,n_list+1):
        num = (i ** 2)
        num = num + i +2
        num = num/2
        list.append(num)
    list.pop()
    print(f"Here's the list containing first {n_list} numbers of Lazy Caterer's series{list}")

def menu():
    print("Welcome to the number sequence generator program!")
    print("Here are your choices:\n1. Fibonacci Sequence\n2. Catalan Sequence\n3. Lazy Caterer's Sequence")




quit = False
while not quit:
    menu()
    n = int(input('Enter your choice:'))
    while n < 1 or n > 3:
        n = int(input("Invalid entry. Re-enter your choice:"))
    if n ==1:
        fib()
        yn = input("Would you like to play the game again? Enter yes or no:")
        if yn== 'no':
            print('Thanks for using the program!Goodbye!')
            quit = True
            break
        elif yn == 'yes':
            
            continue
    elif n ==2:
        catalan()
        yn = input("Would you like to play the game again? Enter yes or no:")
        if yn == 'no':
            print('Thanks for using the program!Goodbye!')
            quit = True
            break
        elif yn == 'yes':

            continue
    elif n ==3:
        lazy()
        yn = input("Would you like to play the game again? Enter yes or no:")
        if yn == 'no':
            print('Thanks for using the program!Goodbye!')
            quit = True
            break
        elif yn == 'yes':

            continue

