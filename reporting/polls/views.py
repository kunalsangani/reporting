from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render

from .models import Report

# Create your views here.

def index(request):
	latest_reports = Report.objects.order_by('-pub_date')[:5]
	return render(request, 'polls/index.html', {
		'latest_reports' : latest_reports,
	})
	# template = loader.get_template('polls/index.html')
	# return HttpResponse(template.render({
	# 	'latest_reports' : latest_reports,
	# }, request))

def detail(request, report_id):
	try:
		report = Report.objects.get(id=report_id)
	except Report.DoesNotExist:
		raise Http404("Report does not exist")
	return render(request, 'polls/detail.html', {
		'report' : report
	})

def results(request, report_id):
	response = "You're looking at the results of report %s"
	return HttpResponse(response % report_id)