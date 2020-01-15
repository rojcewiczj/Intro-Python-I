"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(type(sys.argv))
a = sys.argv
for x in range(len(a)):
    print (a[x]),
# Print out the OS platform you're using:
# YOUR CODE HERE
import subprocess
osVersion =  sys.platform
print(osVersion)
# Print out the version of Python you're using:
# YOUR CODE HERE
pythonVersion = sys.version
print(pythonVersion)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
getID = (os.getpid())
print(getID)

# Print the current working directory (cwd):
# YOUR CODE HERE
getCWD = (os.getcwd())
print(getCWD)
# Print out your machine's login name
# YOUR CODE HERE
getLoginName = (os.getlogin())
print(getLoginName)