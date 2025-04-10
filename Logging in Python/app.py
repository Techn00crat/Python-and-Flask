import logging


## Basic logging settings

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler("app1.log"),
        logging.StreamHandler(),
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a, b):
    logger.debug(f"Adding {a} and {b}")
    return a+b

def subtract(a, b):
    logger.debug(f"Subtracting {a} and {b}")
    return a-b

def multiply(a, b):
    logger.debug(f"Multiplying {a} and {b}")
    return a*b

def divide(a, b):
    try:
        logger.debug(f"Dividing {a} and {b}")
        return a/b
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
 
add(10,15)
subtract(10,15)
multiply(10,15)
divide(20,10)

