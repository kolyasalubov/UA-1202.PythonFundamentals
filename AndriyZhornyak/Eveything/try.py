import logging
logging.basicConfig(filename='cdl.log',filemode='w',
format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

# import logging
# logging.basicConfig(format='%(process)d-%(levelname)s-%(asctime)s-%(message)s', level=logging.INFO)
# logging.info('Admin logged in')
# logging.warning('This is a Warning)


# import logging
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message)