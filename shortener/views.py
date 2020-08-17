from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.views import View

from .models import myURLSh

def myURLSh_redirect_view(request, shortcode=None, *args, **kwargs):
	#try:
	#	obj = myURLSh.objects.get(shortcode=shortcode)
	#except:
	#	obj = myURLSh.objects.all().first()
	obj = get_object_or_404(myURLSh, shortcode=shortcode)
	return HttpResponse("Hello {sc}".format(sc=obj.url))

class myURLShrRedirectView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(myURLSh, shortcode=shortcode)
		return HttpResponse("Hello again {sc}".format(sc=obj.url))