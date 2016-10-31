#!/usr/bin/env python
"""
Utility for remotely sharing slides over a network

Usage:
   slides load_deck (-p <slide_path>) (-i <index_file>) [-t <slideshow_title>]
   slides publish <network_location>
   slides start
   slides end
   slides next
   slides prev
   slides goto <slide_number>
   slides [-h | --help | --version]

Options:
   -p --path   Input path to slide files (JPEG or PNG)
   -i --index  File containing an index of slides in the appropriate order
   -h --help   Prints this help message
"""
__all__ =['slides','commandline']

from slides import *

