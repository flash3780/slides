#!/usr/bin/env python

import setuptools
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
   install_requires = [
      'os',
      ]
   entry_points     = {
                      'console_scripts': [
                         'slides.commandline:main',
                         ]
                      }
   )
