# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py100',
    version='0.1',
    description='VT100 escape sequences wrapper',
    long_description=long_description,
    url='https://github.com/pboardman/py100',
    author='Pascal Boardman',
    author_email='pascalboardman@gmail.com',
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='terminal DEC escape sequence wrapper',
    packages=['py100']
)
