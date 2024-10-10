import logging

# to stdout by default
logging.basicConfig(
    filename="app.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
# Params:
# filemode    - Default 'a' for append
# format      - String structure
# level       - Severity level

logging.debug("This is a debug message")
logging.info("This is an info message")
# -----------------------------------------------
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
logging.exception() #Similar to logger.error() but includes a stack trace.

# String formatting
name = "John"
logging.error("%s raised an error", name) # Can do string formatting


try:
    c = 1 / 0
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
    # same as logging.exception("Exception occurred") same level as error

"""
---------------project wide config
https://towardsdatascience.com/why-and-how-to-set-up-logging-for-python-projects-bcdd4a374c7a

https://towardsdatascience.com/basic-to-advanced-logging-with-python-in-10-minutes-631501339650
"""