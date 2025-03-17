import logging
import os
import sys

location=os.getcwd()

def loggen1():
    logging.basicConfig(
            filename=location+"/app.log",
            filemode='a',  # Append mode (default)
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
    )


    logger = logging.getLogger()
    print(logger)

    return logger



