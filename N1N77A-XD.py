

        




import os, sys
os.system('git pull')

try:

    __import__("bypass").Main()

except Exception as e:

    exit(str(e))
