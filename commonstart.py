import bearoom
from bearoom import bear

print("\nGame: RUN FROM THE REAL\n")
print("\t\tYou find yourself stuck outside the real world.")
print("\t    You don't know if you're dreaming or if you're awake.")
print("\tIf you die, you may wake up from the nightmare of your own brain") 
print("\t\t\t\t\tOR") 
print("\t\t    You might never wake up ever again")

print("Enter which room u want to go to: 1- bear room, 2 - monster room")
a=int(input())
obj = bear()
def choice():
    if a==1:
        obj.prints()
choice()