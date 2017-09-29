from __future__ import absolute_import
import re
from .us_states import STATES_NORMALIZED, USPS_CHOICES

zip_re = "(?P<zip5>\d{5})(?:\s*-\s*(?P<plus4>\d{4}))?"
state_re = "|".join(u[0] for u in USPS_CHOICES)
city_state_zip_re = "^(?P<city>[\w\.\s]+),\s+(?P<state>({}))\s+(?P<zip>{})$".format(
        state_re, zip_re)

class AddressException(Exception):
    pass

def normalize_zip(code):
    match = re.match(zip_re, code)
    if match.group("plus4"):
        return u"{}-{}".format(match.group("zip5"), match.group("plus4"))
    return match.group("zip5")


def parse_address(address):
    """
    Take a multiline textual address, and return a dictionary of components of the form:
    {
        "name": <string>,
        "organization": <string>,
        "address1": <string>,
        "address2": <string>,
        "address3": <string>,
        "city": <string>,
        "state": <2 letter postal code>,
        "zip": <zip, potentially with +4>
    }
    """
    # Split address string.
    parts = [a.strip() for a in address.strip().split("\n")]
    if len(parts) < 3:
        raise AddressException("Less than 3 lines: {}".format(repr(address)))
    parsed = {
        u"name": parts.pop(0)
    }

    # zip on separate line? put it on previous line for regular parsing.
    if re.match("^{}$".format(zip_re), parts[-1]):
        postcode = parts.pop(-1)
        parts[-1] = "{} {}".format(parts[-1], postcode)

    # Remove U.S.A. country
    if re.match("U\.?S\.?A\.?", parts[-1]):
        parts.pop(-1)

    # Too many lines? augment name.
    if len(parts) > 4:
        parsed["name"] = "{} {}".format(parsed["name"], parts.pop(0))
    # Still too many? Add organization.
    if len(parts) > 4:
        parsed["organization"] = parts.pop(0)
    # Still too many? Give up.
    if len(parts) > 4:
        raise AddressException("Too many lines: {}".format(repr(address)))

    # Now we should only have address1 etc. and city/state/zip line.
    # Pull out address1, address2, etc parts.
    count = 1
    while len(parts) > 1:
        parsed[u"address{}".format(count)] = parts.pop(0)
        count += 1

    city_state_zip = parts[0]
    match = re.match(city_state_zip_re, city_state_zip)
    if match:
        parsed[u"city"] = match.group("city")
        parsed[u"state"] = match.group("state")
        parsed[u"zip"] = normalize_zip(match.group("zip"))
    else:
        # Look for a zip to normalize out.
        search = re.search(zip_re, city_state_zip)
        if search:
            city_state = city_state_zip[0:search.start(1)].strip()
            parsed[u"zip"] = normalize_zip(search.group(0))
        else:
            raise AddressException("Unmatched zip: {}".format(repr(address)))

        # Look for a state to normalize out.
        cs = [a for a in re.split("[^\w.]", re.sub("[\.]", "", city_state)) if a]
        if cs[-1].lower() in STATES_NORMALIZED:
            parsed[u"state"] = unicode(STATES_NORMALIZED[cs[-1].lower()])
            # Replace once from the right.  The tricky [::-1]'s are to flip
            # both the original and repalcement strings, so that we can replace
            # right-to-left, and then flipping the result back around.
            parsed[u"city"] = city_state[::-1].replace(cs[-1][::-1], "", 1)[::-1].rstrip(", ")
        elif " ".join(cs[-2:]).lower() in STATES_NORMALIZED:
            parsed[u"state"] = STATES_NORMALIZED[" ".join(cs[-2:]).lower()]
            parsed[u"city"] = city_state.replace(cs[-1], "").replace(cs[-2], "").rstrip(", ")
        else:
            raise AddressException("Unmatched city/state/zip: {}".format(repr(address)))
    return parsed

def format_address(parsed):
    order = ("name", "organization", "address1", "address2", "address3")
    parts = [parsed[o] for o in order if o in parsed]
    parts.append(u"{}, {}  {}".format(parsed["city"], parsed["state"], parsed["zip"]))
    return u"\n".join(parts)

def _parse_all(addresses):
    parsed = []
    for a in addresses:
        try:
            parsed.append(parse_address(a))
        except AddressException as e:
            print(e.message)
    return parsed


