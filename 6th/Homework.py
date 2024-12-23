num=int(input("Enter the number:"))
def ev_odd():
    if num%2:
        print("is odd")
    elif num%3:
        print("is even")
    else:
        print('is not valid number')

ev_odd()