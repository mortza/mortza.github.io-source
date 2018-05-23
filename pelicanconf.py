#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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

# Blogroll
LINKS = (
	('Twitter', 'https://twitter.com/#'),
	)

# Social widget
SOCIAL = (('Twitter', 'https://twitter/#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = './pelican-semantic-ui'
