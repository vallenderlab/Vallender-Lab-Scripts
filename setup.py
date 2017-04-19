# Used:
# https://github.com/pypa/sampleproject/blob/master/setup.py
# https://github.com/biopython/biopython/blob/master/setup.py
# TODO-ROB: 1.  Generate a Template BioSQL database using sqlite3
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import os
import tablib
home = path.abspath(path.dirname(__file__))
name = 'Orthologs-Project'

PACKAGES = [
    'lib',
    'lib.scripts',
    'lib.scripts.biosql',
    'lib.scripts.blast',
    'lib.scripts.ftp',
    'lib.scripts.genbank',
    'lib.scripts.manager',
    'lib.scripts.multiprocessing',
    'lib.scripts.phylogenetic_analyses'
]

# Get the long description from the README file
with open(path.join(home, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Set up an initial configuration file
# //TODO-ROB: Set up a reconfiguration script for manual movements;  Make the script append to 'init.yaml'
config = tablib.Dataset()
config.headers = ('package', 'location')
config.append([name, home])
with open('config.yaml', 'w') as c_yaml:
    c_yaml.write('init.yaml')

setup(
    name=name,
    description="A project that will help to analyze orthologous genes.",
    version='0.1.0',
    long_description=long_description,
    url='https://github.com/robear22890/Orthologs-Project',
    license='?',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Natural Language :: English'
    ],
    packages=PACKAGES,
    install_requires=[],
)
