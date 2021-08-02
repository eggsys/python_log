from function_log import save_log
class Main():
    def __init__(self) -> None:

        try:
            self.function_error()           
            
        except Exception as e:
            save_log(err_log=e)
            
            pass
    



    def function_error(self):
        print("function title")
        fucntion_name  = self.function_error.__name__
        print(fucntion_name)

        #error_is_here 
        




m = Main()