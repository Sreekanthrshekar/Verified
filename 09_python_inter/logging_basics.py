''' This document demonstrates logging basics '''

import logging

# FIVE LOGGING LEVELS:

# DEBUG: Detailed information, typically of interest only when diagnosing problems

# INFO: Confirmation that things are working as expected.

# WARNING:    An indication that something unexpected happened,
            # or indicative of some problem in near future.
            # (e.g., 'disk space low')
            # The software is still working as expected.

# ERROR:   Due to a more serious problem,
         # the software has not been able to perform some function.

# CRITICAL:   A serious error, indicating that the program itself may be
            # unable to continue running.


# LOG RECORD ATTRIBUTES -
# https://docs.python.org/3/library/logging.html?highlight=logrecord%20attributes


logging.basicConfig(filename = './09_python_inter/arith.log',level=logging.DEBUG,
                    format='%(levelname)s:%(message)s')

def add(num_1,num_2):
    ''' Add function '''
    return num_1 + num_2

def subtract(num_1,num_2):
    ''' Subtract function '''
    return num_1 - num_2

def multiply(num_1,num_2):
    ''' Multiply function '''
    return num_1 * num_2

def divide(num_1,num_2):
    ''' Divide function '''
    if num_2 == 0:
        raise ValueError('cannot divide by zero')
    return num_1 / num_2

NUM_1 =100
NUM_2 =20

ADD_RESULT = add(NUM_1,NUM_2)
logging.debug(f"Add: {NUM_1} + {NUM_2} = {ADD_RESULT}")

SUB_RESULT = subtract(NUM_1,NUM_2)
logging.debug(f"Subtract: {NUM_1} - {NUM_2} = {SUB_RESULT}")

MUL_RESULT = multiply(NUM_1,NUM_2)
logging.debug(f"Multiply: {NUM_1} * {NUM_2} = {MUL_RESULT}")

MUL_RESULT = divide(NUM_1,NUM_2)
logging.debug(f"Divide: {NUM_1} / {NUM_2} = {MUL_RESULT}")
