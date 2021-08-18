import bearoom
from bearoom import bear

print("enter which room u want to go to: 1- bear room, 2 - monster room")
a=int(input())
obj = bear()
def choice():
    if a==1:
        obj.prints()
choice()