import sys
import json
import pprint

from addresscleaner import parse_address
from collections import OrderedDict

order = ['name', 'organization', 'address1', 'address2', 'address3', 'city', 'state', 'zip']

def main(filename):
    with open(filename) as fh:
        data = json.load(fh)

    for d in data:
        try:
            parsed = parse_address(d)
        except Exception:
            continue
        dct = OrderedDict()
        for key in order:
            if key in parsed:
                dct[key] = parsed[key]
        print(d.encode('utf-8'))
        print("----")
        print(json.dumps(dct, indent=2).encode('utf-8'))
        print("====")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Requires one argument: a json file of addresses to read."
        sys.exit(1)
    main(sys.argv[1])
