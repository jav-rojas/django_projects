  
import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html
# python3 manage.py runscript many_load

from unesco.models import Site, State, Region, Iso, Category

def run():
    fhand = open('unesco/unesco.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Category.objects.all().delete()

    # Format
    # 0 - name
    # 1 - description
    # 2 - justification
    # 3 - year
    # 4 - longitude
    # 5 - latitude
    # 6 - area_hectares
    # 7 - category
    # 8 - states
    # 9 - region
    # 10 - iso

    for row in reader:
        print(row)

        category, created = Category.objects.get_or_create(name=row[7])
        iso, created = Iso.objects.get_or_create(name=row[10])
        region, created = Region.objects.get_or_create(name=row[9])
        state, created = State.objects.get_or_create(name=row[8], region=region, iso=iso)

        # Para columnas que pueden ser vacías:
        # Año
        try:
            year=int(row[3])
        except:
            year=None
        # Area_hectares
        try:
            area_hectares=int(row[6])
        except:
            area_hectares=None

        site, created = Site.objects.get_or_create(name=row[0], description=row[1], justification=row[2], year=year, longitude=row[4], latitude=row[5], area_hectares=area_hectares, category=category, state=state)