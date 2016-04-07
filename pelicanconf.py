#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'OVER'
SITENAME = u"Over Blog"
SITEURL = 'http://127.0.0.1:8000'


SITETITLE = AUTHOR
SITESUBTITLE = u'Developer'
SITEDESCRIPTION = u'%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = u'http://7xofqa.com1.z0.glb.clouddn.com/myblog.png'
FAVICON = u'http://7xofqa.com1.z0.glb.clouddn.com/favicon.ico'

ROBOTS = u'index, follow'

THEME = u'themes/Flex'
PATH = u'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'en'
OG_LOCALE = u'zh_CN'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d(%A) %H:%M')

#FEED_ALL_ATOM = 'feeds/all.atom.xml'

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

LINKS = ((u'友情推荐', 'http://blog.just4fun.site/index.html'),)

SOCIAL = (('weixin', 'https://wx.qq.com'),
          ('github', 'https://github.com/lyxstudy'),
          ('weibo', 'http://weibo.com/u/2108251924'),
          ('qq', 'http://user.qzone.qq.com/958345510'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

#CC_LICENSE = {
  #  'name': 'Creative Commons Attribution-ShareAlike',
  #  'version': '4.0',
  #  'slug': 'by-sa'
#}

COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 10

#STATUSCAKE = {
 #   'trackid': 'test-test',
  #  'days': 7
#}

RELATIVE_URLS = False

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 5

#DISQUS_SITENAME = "test-test"
#GOOGLE_ANALYTICS = "UA-XXXXXX-X"
#ADD_THIS_ID = 'ra-XX3242XX'

USE_LESS = True
