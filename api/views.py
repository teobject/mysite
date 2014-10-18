# Create your views here.
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from mysite.api.models import IpAddressTable

def ipall(request, ip-id):
    try:
        egg = IpAddressTable.objects.get(id=ip-id)
    except IPAddressTable.DoesNotExist:
        return HttpResponseNotFound(mimetype='application/json')

    json = serializers.serialize('json', egg, ensure_ascii=False)
    return HttpResponse(json, mimetype='application/json')
