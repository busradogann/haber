from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Haber
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic.edit import CreateView 
from django.contrib.auth.models import User 
from django.http import JsonResponse 


def validate_username (request):
	if request.method == 'POST':
		username = request.POST['username']
		data = {
			'status': 200,
			'is_taken': User.objects.filter(username__iexact=username).exists(),}
	return JsonResponse(data)


class SignUpView ( CreateView ): 
	template_name = 'signup.html' 
	form_class = UserCreationForm


def haber(request):
	haberler = Haber.objects.filter(yayinlanma_tarihi__lte=timezone.now()).order_by('yayinlanma_tarihi')
	return render(request, 'haber.html', {'haberler':haberler})


def detail(request, pk):
	haber = get_object_or_404(Haber, pk=pk)
	data = {
		'status' : 200,
		'baslik' : haber.baslik,
		'icerik' : haber.icerik,
		'yayinlanma_tarihi' : haber.yayinlanma_tarihi,
		}
	return JsonResponse(data)






























