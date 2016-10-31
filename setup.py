#!/usr/bin/env python

from setuptools import setup, find_packages

import slides

description, long_description = slides.__doc__.split('\n',1)

setup(
   name             = 'slides',
   version          =    '0.1',
   description      = description.strip(),
   long_description = long_description.strip(),
   author           = 'Christopher K. Hubley',
   author_email     = 'c_hubley@hotmail.com',
   url              = 'https://github.com/flash3780/slides',
   classifiers      = [
      'Development Status :: 1 - Planning',
      'Environment :: Console',
      'License :: OSI Approved :: GNU General Public License'
         'v3 or later (GPLv3+)',
      'Topic :: Office/Business',
      ],
   packages         = find_packages(),
   test_suite       = 'nose.collector',
   tests_require    = ['nose'],
   install_requires = [
      'blessings',
      'docopt',
      ],
   entry_points     = {'console_scripts': ['slides = slides.commandline:main']},
   )
