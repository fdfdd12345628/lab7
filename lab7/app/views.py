from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Data
from django.http import HttpResponse


@csrf_exempt
@require_http_methods(['POST'])
def set(request, key):
    key=key[:256]
    print("set key: "+key)
    data_filter=Data.objects.filter(key=key)
    if data_filter.exists():
        data_object=data_filter[0]
    else:
        data_object=Data(key=key)
    # print(request.POST)
    try:
        data_object.data=request.POST['value'][:256]
        print('set value: '+data_object.data)
    except:
        return HttpResponse('no value', status=403)
    data_object.save()
    for i in Data.objects.all():
        # print(i.key)
        # print(i.data)
        pass
    print('')
    return HttpResponse('OK')


@csrf_exempt
@require_http_methods(['GET'])
def get(request, key):
    key=key[:256]
    print('get key: '+key)
    data_filter = Data.objects.filter(key=key)

    print(data_filter)
    if data_filter.exists():
        data_object = data_filter[0]
    else:
        return HttpResponse('key not found!')
    print('get value: '+data_object.data)
    return HttpResponse(data_object.data)
