# -*- coding: utf-8 -*-

BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'

ROBOTSTXT_OBEY = False
HTTPCACHE_ENABLED = True

ITEM_PIPELINES = {
'amazon.pipelines.AmazonItemPipeline': 0
}