#!/usr/bin/env python
"""
Slides module for manipulating slides in a slideshow.

"""

import os

class Slide(object):

    def __init__(self,slide_path,slide_filename,index):
        self.slideindex= index
        self.slidelink = os.path.join(validate_file( slide_path, slide_filename ))

def validate_path(slide_path):
    """Validates a path"""

    try:
        os.isdir(slide_path)
    except OSError as err:
        print('OS error: {0}'.format(err))
    full_slide_path = os.path.abspath(slide_path)
    return(full_slide_path)

def validate_file(slide_path,slide_filename):
    """Verifies that a file exists"""

    full_slide_path = validate_path(slide_path)
    try:
        os.path.isfile(join(full_slide_path,slide_filename))
    except OSError as err:
        print('OS error: {0}'.format(err))
    return(full_slide_path,slide_filename)

def update_slide_data(**kwargs):
    """Updates persistent slide data."""

def load_deck(index_file,slide_path):
    """Loads a slide deck from an index file"""

def publish(network_location):
    """Publishes slides to a location on the network"""

def goto(slide):
    """Changes the current slide."""
