from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import threading
import time
class main():

    def __init__(self) -> None:
        self.window()
        thr_count = threading.Thread(target=self.countdown, args=(), kwargs={}, name='thread_function')
        thr_count.start()
        

    def window(self):
        #app = QApplication(sys.argv )
        #win = QMainWindow()
        #win.setGeometry(200, 200, 300, 300)
        #win.setWindowTitle("Egg's Screen test")

        #self.count_val = 10
        #self.label = QtWidgets.QLabel(win)
        #self.label.setText(str(self.count_val))
        #self.label.move(50,50)
        #win.show()
        #sys.exit(app.exec_())
        self.count_val = 10
        print("window")

    def countdown(self):
        print("counting down")
        while(self.count_val > 0):
            self.count_val = self.count_val - 1
            print(self.count_val)
            time.sleep(1)
        
        
        

m = main()