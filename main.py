from screen_01 import run
import time
class Main():
    def __init__(self) -> None:
        print("init")
        
    def start(self):
        self.run = run()
        x = run.createScreen(self)

    def stop(self):
        print("stop")

m = Main()
m.start()    
time.sleep(5)   
m.stop()


