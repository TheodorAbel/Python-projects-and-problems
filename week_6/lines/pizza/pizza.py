import sys
import csv
from tabulate import tabulate

if len(sys.argv)<2:
    sys.exit("Too few command line argument")
elif len(sys.argv)>2:
    sys.exit("Too many command line argument")
else:
    if '.csv' not in sys.argv[1]:
        sys.exit("Not in csv format")
    else:
        try:
            with open(sys.argv[1]) as file:
                reader=csv.DictReader(file)
                table=[]
                header=[]
                for row in reader:
                    table.append(row)
                for head in table[0].keys():
                    header.append(head)

                print(tabulate(table,headers="keys",tablefmt="grid"))


        except FileNotFoundError:
            sys.exit("File not found")
