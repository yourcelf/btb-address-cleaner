# Betwen the Bars address cleaner

This is a simple library to clean and normalize textual addresses.  It is
biased toward the sorts of addresses people in prison are given.

## Example usage

    from addresscleaner import parse_address, format_address

    >>> parsed = parse_address("""John Dough
    ... \#1234567
    ... 7819 228th St.
    ... Raiford, FL 32026-1120""")
    >>> print parsed
    {'name': 'John Dough', 'address1': '#1234567', 'address2': '7819 228th St.', 'city': 'Raiford',  'state': 'FL', 'zip': '32026-1120'}

    >>> format_address(parsed)
    u'John Dough\n#1234567\n7819 228th St.\nRaiford, FL  32026-1120'

An exception of type ``addresscleaner.AddressException`` is raised if the
parser is unable to figure out something about the address.  The exception's
message tries to explain as much as possible where it went wrong.

