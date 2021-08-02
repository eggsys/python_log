import logging

def save_log(**kwargs):
    
    LOG_FILE_PATH = 'log/logfile_path'


    Error_code = kwargs.get('err_log',"default value")
    logging.basicConfig(filename=LOG_FILE_PATH,
                            filemode='a',                        
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            level=logging.DEBUG)
   
    logging.error(Error_code)
    logging.getLogger('Smart Check-in')



# format   : to format your log Formation 

# file_mode  a = append the messages from earlier runs will not lost. 
#            w = Write : the messages from earlier runs are lost. 


## REF : https://docs.python.org/3.7/howto/logging.html#logging-basic-tutorial



## level ## 
#DEBUG     Detailed information, typically of interest only when diagnosing problems.
#INFO       Confirmation that things are working as expected.
#WARNING     An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
#ERROR   Due to a more serious problem, the software has not been able to perform some function.
#CRITICAL  A serious error, indicating that the program itself may be unable to continue running.