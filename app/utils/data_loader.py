import json

from alembic import op
from sqlalchemy import MetaData, Table


def load_country_data():
    country_file = open('resources/data/countries.json', encoding="utf8")
    country_data = json.load(country_file)
    print('Loading ', len(country_data['countries_data']), ' countries to database.')
    countries_data = list()
    for country in country_data['countries_data']:
        countries_data.append({
            "country_code": country['isoAlpha3'],
            "country_name": country['name'],
            "country_flag": country['flag']
        })

    country_file.close()

    meta = MetaData(bind=op.get_bind())
    meta.reflect(only=('country',))
    country_table = Table('country', meta)
    op.bulk_insert(country_table, countries_data, True)
    print('Loaded ', len(countries_data), ' countries to database.')