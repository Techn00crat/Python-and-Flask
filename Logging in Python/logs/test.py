from logger import logging

def add(x, y):

    logging.debug(f"Adding {x} and {y}")
    return x+y

logging.debug("the addition function is called")
add(10,15)