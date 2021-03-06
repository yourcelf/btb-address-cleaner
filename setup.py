import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="addresscleaner",
    version="0.1.0",
    author="Charlie DeTar",
    author_email="cfd@media.mit.edu",
    url="https://github.com/yourcelf/btb-address-cleaner",
    long_description=read('README.md'),
    description="Utility for normalizing (Prisoner-centric) street addresses",
    license='BSD',
    packages=['addresscleaner'],
)
