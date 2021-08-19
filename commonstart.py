import time, sys
from bearoom import bear

def begin():
    
    starttext="""You find yourself stuck outside the real world.
            You don't know if you're dreaming or if you're awake.
        If you die, you may wake up from the nightmare of your own brain
                                        OR
                    You might never wake up ever again
        """
    
    for char in starttext:
        sys.stdout.write(char)
        time.sleep(0.03)
        


