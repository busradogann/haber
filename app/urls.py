from django.urls import path
from . import views


urlpatterns = [
    path('', views.haber, name='haber'),
    path('signup' , views . SignUpView . as_view (), name = 'signup' ), 
	path('ajax/validate_username/' , views . validate_username , name = 'validate_username' ),
]