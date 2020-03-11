import sys
import logging

def err_handle():
  return f'Error: {sys.exc_info()[0]}. {sys.exc_info()[1]}, line: {sys.exc_info()[2].tb_lineno}'

try:
  a + b
except Exception as e:
  logging.error(err_handle())
  