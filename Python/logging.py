import logging

# to stdout by default
logging.basicConfig(filename='app.log',
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
# -----------------------------------------------
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

name='John'
logging.error('%s raised an error', name)


level:name:message


try:
  c = 1 / 0
except Exception as e:
  logging.error("Exception occurred",
                exc_info=True)

  # same as logging.exception("Exception occurred") same level as error

# Params:
#     level   -   Severity level
#     filename    -
#     filemode    - default a for append
#     format      -