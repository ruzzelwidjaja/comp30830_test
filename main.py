import socket
import os
import platform
import multiprocessing
import psutil

print('Name of machine: ',socket.gethostname())
print('Operating SystemL ', platform.system())
print('Operating System Version:', platform.release())
print('Number of CPUs: ', multiprocessing.cpu_count())
print('Amount of memory: ', psutil.virtual_memory().total)
print('RAM memory used(%): ', psutil.virtual_memory()[2])
print('IP address of machine ', socket.gethostbyname(socket.gethostname()))
