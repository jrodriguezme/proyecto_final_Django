from .models import Formato

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getFormato(request):
	formato=Formato.objects.filter(pedido_id=request.POST.get('pedido_id',''))
	formato_obj=serializers.serialize('python',formato)
	return JsonResponse(formato_obj,safe=False)