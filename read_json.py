import json
from pprint import pprint

with open('DATA/presidents.json') as pres_in:
    pres_data = json.load(pres_in)

pprint(pres_data)
print('=' * 60)

pres_list = pres_data['presidents']

for pres in pres_list:
    print(pres['fname'], pres['lname'], pres['birthstate'])

json_data = """
[
  {
        "num":1,
        "lname":"Washington",
        "fname":"George",
        "dstart":"1789-04-30",
        "dend":"1797-03-04",
        "birthplace":"Westmoreland County",
        "birthstate":"Virginia",
        "dbirth":"1732-02-22",
        "ddeath":"1799-12-14",
        "party":"no party"
    },

    {
        "num":2,
        "lname":"Adams",
        "fname":"John",
        "dstart":"1797-03-04",
        "dend":"1801-03-04",
        "birthplace":"Braintree, Norfolk",
        "birthstate":"Massachusetts",
        "dbirth":"1735-10-30",
        "ddeath":"1826-07-04",
        "party":"Federalist"
    },

    {
        "num":3,
        "lname":"Jefferson",
        "fname":"Thomas",
        "dstart":"1801-03-04",
        "dend":"1809-03-04",
        "birthplace":"Albermarle County",
        "birthstate":"Virginia",
        "dbirth":"1743-04-13",
        "ddeath":"1826-07-04",
        "party":"Democratic - Republican"
    }
]
"""

print()

data = json.loads(json_data)

pprint(data)



