from commonstart import*
from extrafuncs import difftimedelays
import random
import time
begin()

time.sleep(1.5 )

    
print("\nPick an option to decide your fate:")
inp1=input("1. Solve a PHD level integration problem\n2. Let a dice decide your fate\n")

obja=difftimedelays()
obja.dotdot()

while True:
    if inp1==1:
        print("haha lol u wont be able to solve it anyways dumbo, it's upto the dice to decide your fate")
        print("AND the dice gives you")
        obja.dotdot()
        n=random.randint(1,6)
        print(n)
        break

    elif inp1==2:
        print("AND the dice gives you")
        obja.dotdot()
        n=random.randint(1,6)
        print(n)
        break

if n < 3:
    print("You have entered the BEAR room")
else:
    print("You have entered the MONSTER room")    