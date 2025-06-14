import sys
from src.logger import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #gives the exact error and location of error in the script
    file_name = exc_tb.tb_frame.f_code.co_filename #custom handling exception doc can find in docs
    error_message="error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error)
                                                                                                           
    )

    return error_message                                                                         

class CustomException(Exception): #creating acustomexception on your own
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) #calls the super class
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message