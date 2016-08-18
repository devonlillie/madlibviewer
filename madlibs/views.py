from django.shortcuts import render
from django.core.urlresolvers import reverse

from .models import Madlib,Field
from .forms import MadlibForm


def view_madlib(request,title):
	madlib = Madlib.objects.get(title=title)
	return render(request,'madlibs/madlib.html',{'madlib':madlib})

def home_page(request):
	if request.POST:
		if validate_form(request.POST):
			f = MadlibForm(request.POST)
			f.save()
			return view_madlib(request,request.POST['title'])
	if request.GET:
		return render(view_madlib,'madlibs/madlib.html',{'title':request.GET.get('mad')})
	return render(request,'madlibs/home.html', {'hist':Madlib.objects.all().order_by('created_on')[:5]})

def validate_form(params):
	if params['title']=='':
		return False
	if params['text']=='':
		return False
	return True

def render_madlib(m):
	txt = m.text 
	t = m.t
	return {'title':t,'text':txt}

def match_case(origin,fill):
	if origin.istitle():
		fill = fill.title()
	elif origin.isupper():
		fill = fill.upper()
	else:
		fill = fill.lower()
	return fill