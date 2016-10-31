#!/usr/bin/env python
""" Utility for remotely sharing slides over a network

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

import blessings
from docopt import docopt

import slides.load_deck
import slides.publish
import slides.nextslide
import slides.prevslide
import slides.gotoslide
import slides.firstslide
import slides.lastslide

def main():
   args = docopt(__doc__)
   terminal = blessings.Terminal(force_styling=True)
   for line in _main(args, terminal):
      print(line)

def _main(args, terminal)
   t = terminal
   if args['load_deck']:
      screen_output, errormsg =
         slides.load_deck(args['<indexfile>'])
      print(t.(screen_output+'\n'))

   if args['publish']:
      screen_output, errormsg =
         slides.publish(args['<network_location>'])
      print(t.(screen_output+'\n'))

   if args['start']:
      screen_output, errormsg =
         slides.goto('start')
      print(t.(screen_output+'\n'))
      
   if args['end']:
      screen_output, errormsg =
         slides.goto('end')
      print(t.(screen_output+'\n'))
      
   if args['prev']:
      screen_output, errormsg =
         slides.goto('prev')
      print(t.(screen_output+'\n'))

   if args['next']:
      screen_output, errormsg =
         slides.goto('next')
      print(t.(screen_output+'\n'))

   if args['goto']:
      screen_output, errormsg =
         slides.goto(args['slide_number'])
      print(t.(screen_output+'\n'))
