#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
from jfilters import site_filters
import jinja2

sys.path.append('.')
JINJA_FILTERS = {
    'TagColor': site_filters.getTagColor,
    'zip': site_filters.jinja2_tag_color_zipper,
    'jDate': site_filters.convert_to_jalali_date,
}

AUTHOR = 'Morteza Allahpour'
SITENAME = ''
SITEURL = ''
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'

TIMEZONE = 'Asia/Tehran'
DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'fa'
DISPLAY_PAGES_ON_MENU = True
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LOAD_CONTENT_CACHE = False

# Blogroll
LINKS = (('Twitter', 'https://twitter.com/#'), )

# Social widget
SOCIAL = (('Twitter', 'https://twitter/#'), )

# DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = './pelican-semantic-ui'
