import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command line arguments")

try:
    if not all(arg.endswith('.csv') for arg in sys.argv[1:3]):
        raise FileNotFoundError

    with open(sys.argv[1]) as file, open(sys.argv[2], 'w', newline='') as new_file:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(new_file,fieldnames=["first","last","house"])
        writer.writeheader()

        for row in reader:
            name = row["name"].strip()
            house = row["house"].strip()
            if name.startswith('"') and name.endswith('"'):
                name = name[1:-1]
            parts = [part.strip() for part in name.split(',')]
            first, last = parts
            writer.writerow(
                {"first":f"{last}",
                             "last":f"{first}",
                             "house":f"{house}"
                }
            )

except FileNotFoundError:
    sys.exit("File not found")
