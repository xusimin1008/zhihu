# coding: utf-8
from scrapy import Spider
from scrapy import Request
import django
from django.conf import settings

from .. import config
from ..items import ZhihuAuthorItem


class ZhihuAuthorSpider(Spider):

    name = "zhihu_author"

    def __init__(self, author_id):
        super(ZhihuAuthorSpider, self).__init__()
