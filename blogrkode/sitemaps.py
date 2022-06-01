from django.contrib.sitemaps import Sitemap
from .models import BlogModel
from django.shortcuts import reverse
from django.contrib.sites.models import Site

class blogSitemap(Sitemap):
	# def get_urls(self, site=None, **kwargs):
	# 	site = Site(domain='rkode.tk', name='rkode.tk')
	# 	return super(blogSitemap, self).get_urls(site=site, **kwargs)
	def items(self):
		return BlogModel.objects.all()

	