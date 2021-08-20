import time, sys
from os import system, name
class difftimedelays:

    def dotdot(self):
        print(".")
        time.sleep(1) 
        print(".")
        time.sleep(1) 
        print(".")
        time.sleep(1) 
        print(".")

    def switching(self):
        str = "Switching to the Next Stage "
        str2 = ". . ."

        for char in str:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        
        for char in str2:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.2)

    def clear(self):
        # for windows
        if name == 'nt':
         _ = system('cls')
  
        # for mac and linux(here, os.name is 'posix')
        else:
         _ = system('clear')