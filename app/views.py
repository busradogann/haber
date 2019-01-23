from django.shortcuts import render
from django.utils import timezone
from .models import Haber



def haber(request):
	haber = Haber.objects.filter(yayinlanma_tarihi__lte=timezone.now()).order_by('yayinlanma_tarihi')
	return render(request, 'haber.html', {'haber':haber})