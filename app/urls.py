from django.urls import path
from . import views


urlpatterns = [
    path('', views.haber, name='haber'),
	path('<int:pk>/', views.detail, name='detail'),
    path('signup' , views . SignUpView . as_view (), name = 'signup' ), 
	path('ajax/validate_username/' , views . validate_username , name = 'validate_username' ),
]