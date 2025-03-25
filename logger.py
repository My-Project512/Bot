import logging

def setup_logger():
    """Set up the logger for the application."""
    logger = logging.getLogger('telegram_bot')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('bot_errors.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
