#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

########################
#### BASIC SETTINGS #### 
########################

AUTHOR = u'Kristine M. Yu'

# Site settings
SITESUBTITLE = u'Linguist at UMass Amherst'
SITENAME = u'Kristine M. Yu'
SITEURL = ''

DEFAULT_DATE_FORMAT = '%Y %B %d'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'
LOCALE = 'en_US'

# Set theme
THEME = '../themes/pelican-octopress-theme'

# Ignores emac lock files
IGNORE_FILES =  (['.#*']) 

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins
PLUGIN_PATH = '../pelican-plugins/'
PLUGINS = ['latex', 'neighbors', 'summary']
LATEX = 'article' # Only use LaTeX for selected articles

# Set static paths
STATIC_PATHS = ["blog/img", "blog/data", "blog/videos", "pages/home", "pages/output", "pages/resources", "pages/teaching", "pages/masspros"]

## Set templates 

# List of templates that are used directly to render content. Typically direct templates are used to generate index pages for collections of content (e.g. tags and category index pages).

DIRECT_TEMPLATES = ['blog', 'tag', 'archives']
PAGINATED_DIRECT_TEMPLATES = ['blog']
DEFAULT_PAGINATION = 5

# Tag cloud setup
#TAG_CLOUD_STEPS = 4 # Count of different font sizes in the tag cloud.
#TAG_CLOUD_MAX_ITEMS = 100 # Max number of tags in cloud

######################
#### URL SETTINGS #### 
######################

# Article settings
ARTICLE_URL = "blog/posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/posts/{date:%Y}/{date:%m}/{slug}/index.html"

# Page settings
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Author and category settings
AUTHOR_URL = ''
AUTHOR_SAVE_AS = False # Don't create author file
CATEGORY_URL = ''
CATEGORY_SAVE_AS = False # Don't create category file

# Archive settings
YEAR_ARCHIVE_SAVE_AS = 'blog/posts/{date:%Y}/index.html'
ARCHIVES_SAVE_AS = "archives/index.html"
NEWEST_FIRST_ARCHIVES = False

# Direct template settings
BLOG_SAVE_AS =  'blog/index.html'
#TAG_SAVE_AS =  'tag/index.html'

###################################################
#### THEMING SETTINGS: NAVIGATION AND SIDEBARS #### 
###################################################

# Navigation bar
MENUITEMS = [('output', '/output'),             
             ('teaching', '/teaching'),
             ('resources', '/resources'),
             ('blog', '/blog'),
             ('archives', '/archives')]
DISPLAY_PAGES_ON_MENU = False

# Search box
SEARCH_BOX = True

# Sidebar

#Github include settings
GITHUB_USER = 'krismyu'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Footer

FOOTER_MESSAGE = u'This work is licensed under the <a href="http://creativecommons.org/licenses/by-sa/3.0/" rel="license">CC BY-SA</a>.'


#########################
#### FEED GENERATION #### 
#########################

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


########################################
#### COMMENTING AND SITE STATISTICS #### 
########################################

DISQUS_SITENAME = 'krisyu'

PIWIK_URL = 'www.piwik.krisyu.org'
#PIWIK_SSL_URL = ''
PIWIK_SITE_ID = '2'
