from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .poloniex_server import server

def index(request):
    return render(request, 'poloniex_service/index.html', {})

@csrf_exempt
def public_api(request):
    print('[PUBLIC] {}'.format(request))
    return JsonResponse(server().dispatcher_public(request), safe=False)

@csrf_exempt
def trading_api(request):
    print('[PRIVATE] {}'.format(request.body))
    return JsonResponse(server().dispatcher_trading(request), safe=False)