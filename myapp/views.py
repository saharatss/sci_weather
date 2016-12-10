from django.shortcuts import render

from django.http import HttpResponse
from .models import Weather

from django.http import JsonResponse
import json

# Create your views here.

def append_data(request):
	weather_data = Weather( 
			nodeid	= request.GET['nodeid'], 
			temp 	= float(request.GET['temp']), 
			humi 	= float(request.GET['humi']), 
			israin  = (request.GET['israin'] == "True") 
		)
	weather_data.save()
	return HttpResponse("Recieved", content_type='text/plain')

def show_table(request,nodeid):
	weather_data = Weather.objects.all()
	#.order_by('-nodeid')[:10][::-1]
	data = []
	real_time = ""
	real_temp = 0.0
	real_humi = 0.0
	real_israin = False
	real_nodeid = ""
	for row in weather_data:
		data.append(
			{
				'time'	:row.time, 
				'nodeid':row.nodeid, 
				'temp'	:row.temp, 
				'humi'	:row.humi, 
				'israin':row.israin
			})

	chart_data = []
	nodeid_dic = {}
	for i in weather_data:
		if i.nodeid not in nodeid_dic:
			nodeid_dic[i.nodeid] = 0
		if int(i.nodeid) is int(nodeid):
			real_time = i.time
			real_temp = i.temp
			real_humi = i.humi
			real_israin = i.israin
			real_nodeid = i.nodeid
			chart_data.append({
					#'date'	: "%s %s %s %s %s"%( i.time.hour,i.time.minute,i.time.day,i.time.month,i.time.year),
					'date'	: "%02d %02d %d"%( i.time.day, i.time.month,i.time.year),
					'temp'	: float(i.temp)
				})
			#print "%s %s %s %s %s"%( i.time.hour,i.time.minute,i.time.day,i.time.month,i.time.year)

	#print chart_data

	nodeid_array = []
	for v,k in nodeid_dic.iteritems():
		nodeid_array.append(v)		

	return render(request,"home.html",{
		'data':data,
		'real_time':real_time,
		'real_temp':real_temp,
		'real_humi':real_humi,
		'real_israin':real_israin,
		'real_nodeid':real_nodeid,
		'nodeid_array':nodeid_array,
		'chart_data':json.dumps(chart_data).replace('\"','\'')})

def show_home(request):
	return show_table(request,1)


def data_exchanger(request):
	print request.GET
	nodeid=json.loads(request.GET.get('nodeid'))
	print nodeid
	server_data = {'server_data':[
			{'key':'value0'},
			{'key':'value1'},
	]}
	return JsonResponse( server_data)

def rice_diseases(request):
	return render(request,"rice_diseases.html") 