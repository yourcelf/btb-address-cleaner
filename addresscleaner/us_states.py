# From http://django-localflavor.readthedocs.org/en/latest/
"""
A mapping of state misspellings/abbreviations to normalized
abbreviations, and alphabetical lists of US states, territories,
military mail regions and non-US states to which the US provides
postal service.

This exists in this standalone file so that it's only imported into memory
when explicitly needed.
"""

#: The 48 contiguous states, plus the District of Columbia.
CONTIGUOUS_STATES = (
    ('AL', 'Alabama'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

#: All 50 states, plus the District of Columbia.
US_STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

#: Non-state territories.
US_TERRITORIES = (
    ('AS', 'American Samoa'),
    ('GU', 'Guam'),
    ('MP', 'Northern Mariana Islands'),
    ('PR', 'Puerto Rico'),
    ('VI', 'Virgin Islands'),
)

#: Military postal "states". Note that 'AE' actually encompasses
#: Europe, Canada, Africa and the Middle East.
ARMED_FORCES_STATES = (
    ('AA', 'Armed Forces Americas'),
    ('AE', 'Armed Forces Europe'),
    ('AP', 'Armed Forces Pacific'),
)

#: Non-US locations serviced by USPS (under Compact of Free
#: Association).
COFA_STATES = (
    ('FM', 'Federated States of Micronesia'),
    ('MH', 'Marshall Islands'),
    ('PW', 'Palau'),
)

#: Obsolete abbreviations (no longer US territories/USPS service, or
#: code changed).
OBSOLETE_STATES = (
    ('CM', 'Commonwealth of the Northern Mariana Islands'),  # Is now 'MP'
    ('CZ', 'Panama Canal Zone'),                             # Reverted to Panama 1979
    ('PI', 'Philippine Islands'),                            # Philippine independence 1946
    ('TT', 'Trust Territory of the Pacific Islands'),        # Became the independent COFA states + Northern Mariana Islands 1979-1994
)


#: All US states and territories plus DC and military mail.
STATE_CHOICES = tuple(sorted(US_STATES + US_TERRITORIES + ARMED_FORCES_STATES, key=lambda obj: obj[1]))

#: All US Postal Service locations.
USPS_CHOICES = tuple(sorted(US_STATES + US_TERRITORIES + ARMED_FORCES_STATES + COFA_STATES, key=lambda obj: obj[1]))

#: Normalized versions of state names
STATES_NORMALIZED = {
    'ak': 'AK',
    'al': 'AL',
    'ala': 'AL',
    'alabama': 'AL',
    'alaska': 'AK',
    'american samao': 'AS',
    'american samoa': 'AS',
    'ar': 'AR',
    'ariz': 'AZ',
    'arizona': 'AZ',
    'ark': 'AR',
    'arkansas': 'AR',
    'as': 'AS',
    'az': 'AZ',
    'ca': 'CA',
    'calf': 'CA',
    'calif': 'CA',
    'california': 'CA',
    'co': 'CO',
    'colo': 'CO',
    'colorado': 'CO',
    'conn': 'CT',
    'connecticut': 'CT',
    'ct': 'CT',
    'dc': 'DC',
    'de': 'DE',
    'del': 'DE',
    'delaware': 'DE',
    'deleware': 'DE',
    'district of columbia': 'DC',
    'fl': 'FL',
    'fla': 'FL',
    'florida': 'FL',
    'ga': 'GA',
    'georgia': 'GA',
    'gu': 'GU',
    'guam': 'GU',
    'hawaii': 'HI',
    'hi': 'HI',
    'ia': 'IA',
    'id': 'ID',
    'idaho': 'ID',
    'il': 'IL',
    'ill': 'IL',
    'illinois': 'IL',
    'in': 'IN',
    'ind': 'IN',
    'indiana': 'IN',
    'iowa': 'IA',
    'kan': 'KS',
    'kans': 'KS',
    'kansas': 'KS',
    'kentucky': 'KY',
    'ks': 'KS',
    'ky': 'KY',
    'la': 'LA',
    'louisiana': 'LA',
    'ma': 'MA',
    'maine': 'ME',
    'marianas islands': 'MP',
    'marianas islands of the pacific': 'MP',
    'marinas islands of the pacific': 'MP',
    'maryland': 'MD',
    'mass': 'MA',
    'massachusetts': 'MA',
    'massachussetts': 'MA',
    'md': 'MD',
    'me': 'ME',
    'mi': 'MI',
    'mich': 'MI',
    'michigan': 'MI',
    'minn': 'MN',
    'minnesota': 'MN',
    'miss': 'MS',
    'mississippi': 'MS',
    'missouri': 'MO',
    'mn': 'MN',
    'mo': 'MO',
    'mont': 'MT',
    'montana': 'MT',
    'mp': 'MP',
    'ms': 'MS',
    'mt': 'MT',
    'n d': 'ND',
    'n dak': 'ND',
    'n h': 'NH',
    'n j': 'NJ',
    'n m': 'NM',
    'n mex': 'NM',
    'nc': 'NC',
    'nd': 'ND',
    'ne': 'NE',
    'neb': 'NE',
    'nebr': 'NE',
    'nebraska': 'NE',
    'nev': 'NV',
    'nevada': 'NV',
    'new hampshire': 'NH',
    'new jersey': 'NJ',
    'new mexico': 'NM',
    'new york': 'NY',
    'nh': 'NH',
    'nj': 'NJ',
    'nm': 'NM',
    'nmex': 'NM',
    'north carolina': 'NC',
    'north dakota': 'ND',
    'northern mariana islands': 'MP',
    'nv': 'NV',
    'ny': 'NY',
    'oh': 'OH',
    'ohio': 'OH',
    'ok': 'OK',
    'okla': 'OK',
    'oklahoma': 'OK',
    'or': 'OR',
    'ore': 'OR',
    'oreg': 'OR',
    'oregon': 'OR',
    'pa': 'PA',
    'penn': 'PA',
    'pennsylvania': 'PA',
    'pr': 'PR',
    'puerto rico': 'PR',
    'rhode island': 'RI',
    'ri': 'RI',
    's dak': 'SD',
    'sc': 'SC',
    'sd': 'SD',
    'sdak': 'SD',
    'south carolina': 'SC',
    'south dakota': 'SD',
    'tenn': 'TN',
    'tennessee': 'TN',
    'territory of hawaii': 'HI',
    'tex': 'TX',
    'texas': 'TX',
    'tn': 'TN',
    'tx': 'TX',
    'us virgin islands': 'VI',
    'usvi': 'VI',
    'ut': 'UT',
    'utah': 'UT',
    'va': 'VA',
    'vermont': 'VT',
    'vi': 'VI',
    'viginia': 'VA',
    'virgin islands': 'VI',
    'virgina': 'VA',
    'virginia': 'VA',
    'vt': 'VT',
    'w va': 'WV',
    'wa': 'WA',
    'wash': 'WA',
    'washington': 'WA',
    'west virginia': 'WV',
    'wi': 'WI',
    'wis': 'WI',
    'wisc': 'WI',
    'wisconsin': 'WI',
    'wv': 'WV',
    'wva': 'WV',
    'wy': 'WY',
    'wyo': 'WY',
    'wyoming': 'WY',
}
