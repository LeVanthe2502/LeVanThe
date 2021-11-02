"""
Author: Le Van The
Date: 26/08/2021
Problem:
    Explain what goes on behind the scenes when your computer runs a Python
program.
Solution:
Behind the scenes while executing python programs:
• The interpreter reads the statements and check for syntactical errors. If found any error then it halts the process and return the error message.
• If no error found then the interpreter converts the python statements into low-level language called byte -codes.
• This byte code is executed by a python virtual machine (PVM) and if PVM finds any error then it halts the execution and returns the error message.
• If no error found by PVM then it gives the final output.
    ....
"""