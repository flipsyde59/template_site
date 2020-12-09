from django.http import JsonResponse
from django.http import QueryDict
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .source import sqrt

def from_bytes(byte_str):
    import ast
    dict_str = byte_str.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    return mydata


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, "index.html")
    if request.method == 'PATCH':
        rr = from_bytes(request.read())
        res = sqrt(rr['number'], int(rr['eps']))
        return JsonResponse({'res': res})
