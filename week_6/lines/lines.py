import sys
import os

if len(sys.argv)<2:
    sys.exit("Too few command line")
elif len(sys.argv)>2:
    sys.exit("Too many command line")
else:
    if '.py' not in sys.argv[1]:
       sys.exit("Not python file")
    py_file=sys.argv[1]
    if not os.path.exists(py_file):
        sys.exit("File doesn't exist")
    else:
        count=0
    with open(py_file) as file:
        for line in file:
            stripped_line=line.lstrip()
            if stripped_line.startswith("#"):
                pass
            elif stripped_line=="":
                pass
            else:
                count+=1
        print(count)





