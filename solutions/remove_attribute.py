import json
from pprint import pprint


def remove_attribute(entry, attribute_to_delete='Ticket'):
    if attribute_to_delete in entry:
        del entry[attribute_to_delete]
    return entry


with open('data/titanic.json') as json_file:
    data = json.load(json_file, object_hook=remove_attribute)
    pprint(data[0])
