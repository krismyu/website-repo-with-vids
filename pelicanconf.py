#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kristine M. Yu'
SITENAME = u'Kristine M. Yu'
SITESUBTITLE = u'Linguist at UMass Amherst'
SITEURL = ''

PATH = 'content'

DEFAULT_DATE_FORMAT = '%Y %B %d'
TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Set theme
THEME = '../themes/pelican-bootstrap3'

# Set bootstrap theme
BOOTSTRAP_THEME = 'simplex'
BOOTSTRAP_NAVBAR_INVERSE = 'TRUE'

#ABOUT_ME = 'Hi there.'
#AVATAR = './content/img/emmy-sophie-sideways.jpg'


###################################################
#### THEMING SETTINGS: NAVIGATION AND SIDEBARS #### 
###################################################

# Navigation bar
MENUITEMS = [('About', '/home'),             
             ('Research', '/research'),
             ('Teaching', '/teaching'),
             ('Code', '/code'),
             ('Blog', '/blog')]
DISPLAY_PAGES_ON_MENU = False

# Search box
SEARCH_BOX = True





# Ignores emac lock files
IGNORE_FILES =  (['.#*']) 

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins

PLUGIN_PATHS=['../plugins',]
#PLUGINS = [
#    'neighbors',
#    'latex']
#    'pelican_fontawesome',
#    'pelican_gist',
#    'render_math',
#    'sitemap',
#    ]

# PLUGIN_PATH = '../pelican-plugins/'
# PLUGINS = ['latex', 'neighbors', 'summary']
#LATEX = 'article' # Only use LaTeX for selected articles

# Set static paths
# STATIC_PATHS = ["blog/img", "blog/data", "blog/videos", "pages/home", "pages/output", "pages/resources", "pages/teaching", "pages/masspros"]




# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)


### Twitter
TWITTER_USERNAME = 'linguist_krisyu'
TWITTER_WIDGET_ID = '716655349130989568'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
