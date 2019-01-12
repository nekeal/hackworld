import csv
import sys
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackworld.settings')
django.setup()

from people.models import City

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage {sys.argv[0]} csv_file')
        exit(1)
    with open(sys.argv[1]) as file:
        reader = csv.reader(file, delimiter=';')
        next(reader, None)
        for row in reader:
            if len(row) > 4 and int(row[4]) == 96:
                city = City(name=row[6])
                print(row[6])
                city.save()
