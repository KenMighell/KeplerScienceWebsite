#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import datetime

# If `DEVMODE = True`, show a red warning banner at the top
DEVMODE = False   # pelicanconf-dev.py will override this

CACHE_CONTENT = True

ANALYTICS = ()   # pelicanconf-live.py will override this

AUTHOR = u'Thomas Barclay'
SITENAME = "Kepler &amp; K2"
BANNER_SUBTITLE = "Science Center"
SITEURL = "http://keplerscience.arc.nasa.gov"
SITELOGO = 'images/NASA_logo_vector_lg.png'
SITELOGO_SIZE = 32
FAVICON = 'images/favicon.png'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

PATH = 'content'
THEME = "themes/pelican-bootstrap3-kepler"
BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_FLUID = False

BANNER = "images/kepler-k2-banner.jpg"
HIDE_SITENAME = False

IGNORE_FILES = [
    "README.md",
]

# Enable RSS feeds
FEED_DOMAIN = "http://keplerscience.arc.nasa.gov"
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
# We don't need per-author or per-category or per-translation feeds
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_BREADCRUMBS = False

HIDE_SIDEBAR = True
MD_EXTENSIONS = (['toc'])

# Which static data dirs should be uploaded as part of the website?
STATIC_PATHS = (['images', 'data'])

# Directories that contain html files we want to exclude
# because they are sub-pages included through rst includes
PAGE_EXCLUDES = ['pages/k2-observing/approved-programs']

# The fancy table of contents sidebar requires a plugin
PLUGIN_PATHS = [os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             "plugins")]
PLUGINS = ['extract_toc']

# Defines the menu items in the top bar
MENUITEMS = (
        ('News', 'archives.html'),
        ('The missions', (
            ('Objectives', 'objectives.html'),
            ('Telescope', 'the-kepler-space-telescope.html'),
            ('Science', 'science.html'),
            ('Publications', 'publications.html'),
            ('Conferences', 'conferences.html'),
            )
         ),
        ('K2 observing', (
            ('Overview', 'k2-observing.html'),
            ('Campaign fields', 'k2-fields.html'),
            ('Targets &amp; programs', 'k2-approved-programs.html'),
            ('Data release notes', 'k2-data-release-notes.html'),
            ('Proposal preparation', 'k2-proposing-targets.html'),
            ('Discretionary time', 'k2-ddt.html'),
            ('Microlensing experiment', 'k2-c9.html'),
            )
         ),
        ('Data analysis', (
            ('Data products', 'data-products.html'),
            ('Pipeline', 'pipeline.html'),
            ('Software', 'software.html'),
            ('Related surveys', 'related-surveys.html'),
            )
         ),
        )

# Defines the "key information" box on the front page
KEY_INFORMATION = (
            ('K2: Campaign fields', 'k2-fields.html'),
            ('K2: Observed programs', 'k2-approved-programs.html'),
            ('K2: Proposing targets', 'k2-proposing-targets.html'),
            ('K2: Discretionary time', 'k2-ddt.html'),
            ('Kepler/K2: Data products', 'data-products.html'),
            ('Kepler/K2: Publications', 'publications.html'),
            )

# Defines the "important dates" box on the front page
IMPORTANT_DATES = (
            ('<b>24 Jun 2016</b>',
             'K2 Campaign 8 data release (expected)',
             'data-products.html#k2-product-overview'),
            ('<b>18 Aug 2016</b>',
             'K2 Campaign 12 DDT proposal deadline',
             'k2-ddt.html'),  
            ('<b>23 Sep 2016</b>',
             'K2 GO Cycle 5 Step-1 Deadline',
             'k2-proposing-targets.html#solicitations'),
            ('<b>26 Sep 2016</b>',
             'K2 Campaign 9 data release (expected)',
             'data-products.html#k2-product-overview'),
            ('<b>04 Nov 2016</b>',
             'K2 GO Cycle 5 Step-2 Deadline',
             'k2-proposing-targets.html#solicitations'), 
            ('<b>10 Nov 2016</b>',
             'K2 Campaign 13 DDT proposal deadline',
             'k2-ddt.html'), 
         )

# Defines the "meetings" box on the front page
MEETINGS = (
            ('<b>12-16 Jun 2016</b><br>'
             '228th AAS Meeting',
             'http://aas.org/meetings/aas228'),
            ('<b>3-8 Jul 2016</b><br>'
             'Exoplanets I',
             'http://www.exoplanetscience.org'),    
            ('<b>11-15 Jul 2016</b><br>'
             'TASC2-KASC9 Asteroseismology Workshop',
             'http://www.iastro.pt/research/conferences/spacetk16/'),
            ('<b>17-27 Jul 2016</b><br>'
             'Asteroseismology and Exoplanets: Listening to the Stars and Searching for New Worlds',
             'http://www.iastro.pt/research/conferences/faial2016/'),
            ('<b>19-23 Jun 2017</b><br>'
             'Kepler & K2 SciCon IV: Legacy & Scion',
             '/save-the-date-for-kepler-k2-scicon-iv-june-19-23-2017.html') 
            )

# Defines the "related websites" listing in the footer of all pages
RELATEDSITES = (
            ("Kepler/K2 News and Media Resources",
             'http://www.nasa.gov/mission_pages/kepler/main/index.html'),
            ('Kepler/K2 Education Resources',
             'http://kepler.arc.nasa.gov'),
            ('Kepler/K2 @ Ball Aerospace',
             'http://www.ballaerospace.com/page.jsp?page=72'),
            ('Kepler Data Archive @ MAST',
             'http://archive.stsci.edu/kepler'),
            ('K2 Data Archive @ MAST',
             'http://archive.stsci.edu/k2'),
            ('NASA Exoplanet Archive @ IPAC',
             'http://exoplanetarchive.ipac.caltech.edu'),
            )

SHOW_ARTICLE_AUTHOR = True
DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DATE_MODIFIED = datetime.datetime.now().strftime('%Y-%m-%d')
