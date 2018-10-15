#!/usr/bin/python3

from setuptools import setup

setup(
    name='Cornora',
    version='0.1',
    description='Simple Hotcorner Launcher for X',
    url='https://github.com/pypa/sampleproject',
    author='Nanda Okitavera',
    author_email='codeharuka.yusa@gmail.com',
    packages=["cornora"],
    license='MIT',
    platforms='Linux',
    entry_points={
        'console_scripts': [
              'cornora = cornora.__init__:main'
          ]
    }
)

