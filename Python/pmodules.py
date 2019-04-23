Python modules


# ===== pdb =====
# python debugger

import pdb


pdb.set_trace()  # set breakpoint

# command line commands
w - shows where are you in code
l - show current breakpoint
ll - whole function or frame source code
n - next line
c - leave breakpoint and execute program
s - next line(including function calls)
r - to the end of currently executing function
b [line w] - sets breakpoint

# ===== re =====

# ===== threading =====
# simple usage
from threading import Thread
thread = Thread(target=target_function, args=('function', 'args'))
thread.start()
thread.join()

# ===== logging =====
import logging

logger = logging.getLogger(__name__)  # get or create logger with this filename name))
logger.setLevel(logging.DEBUG)


formatter = logging.Formatter('')
file_handler = logging.FileHandler(filename)  # create file handler to save info to the file
file_nadler.setLevel(DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


formatter options
%(asctime)s - time
%(filename)s - filename
%(funcName)s - function name
%(levelname)s - levelname
%(lineno)d - line
%(message)s - message
%(name)s - logger name


 ===== argparse =====
 Парсер данных ввходимых в командную строку вместе с запуском скрипта

import argparse
# command line parser
parser = argparse.ArgumentParser(description='')  # init parser
parser.add_argument('name', type=int/str, metavar='', help='Help text')
parser.add_argument('--name', type=int/str, metavar='', help='Help text')  # optional arguement
parser.add_argument('-flag', '--name', type=int/str, help='Help text')  # flags
args = parser.parse_args()  # sequence of parced args
print(args.name)  # use args


# ===== decimal =====
from decimal import *

x = Decimal("0.444")
Decimal('1.41421356').quantize(Decimal('1.000'))

# ===== random =====
import random

random.choice()  # chooses random object
random.randrange(start, stop)  # random value from sequence
random.shuffle()  # shuffles sequence(lists, dictionaries) no tuples, strings
random.random()  # random float beetween 0 and 1 (15 decimal places)
random.sample(lst, x)  # random x element outta lst sequence
random.randint(a, b)  # random a <= number <= b

# ===== sys =====
import sys


# ===== os =====
import os

os.name  # os name
os.environ  # dict with os info
os.uname()  #
os.getcwd()  # current dir
os.listdir(path)  # list of files and dirs
os.system(str(command to execute))  # return result code (0 - ok, )
os.walk()

# ===== os.path =====
from os import path

path.abspath(path)  # normalized path
path.join(path1, path2)  # make path from 2 or more paths
path.basename(path)  # return dir name or a file name
path.is_file(path)  # true if the file exists
path.isdir(path)  # true if dir exist
path.splitext(path)  # path and extension
path.splitdrive(path)  # path

# ===== datetime =====

# ===== hashlib =====
import hashlib
# md5(), sha1(), sha224(), sha256(), sha384, sha512()

hashlib.sha255(b'string')  # hashes bytes sequence
hash.digest()  # to get the crypted byte sequence
hash.hexdigest()  # to get crypted string

# ===== http.server =====
# -= command line usage =-
python http.server -m 8000
	-b 127.0.0.1  bind to IP
	--directory /path/to directory/
