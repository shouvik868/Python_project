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
    logger=logging.getLogger(__name__)
    logger.addHandler(sh)
    #print(logger)
    return logger
#loggen().info("okk")