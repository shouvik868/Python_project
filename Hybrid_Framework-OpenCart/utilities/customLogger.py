import logging

def loggen():
    logging.basicConfig(
        filename="./Hybrid_Framework-OpenCart/Logs/automation.log",
        filemode='a',  # Append mode (default)
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        force = True
    )
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger=logging.getLogger()
    logger.addHandler(sh)
    #print(logger)
    return logger
