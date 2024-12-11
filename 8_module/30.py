import os

os.chdir("C:/Users/bjy80/Documents/python/8_module")
dir = os.popen('dir')
print(dir.read())

print(os.listdir())