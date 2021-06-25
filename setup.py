from setuptools import setup
from setuptools import find_packages

setup(
    name='exospectra',
    version='0.0.2',
    packages = find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'pandas',
    ],
    url = "https://github.com/riobanerjee/exospectra"
)