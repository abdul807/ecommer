from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.store,name='store'),
    path('checkout/', views.checkout,name='checkout'),
    path('cart/', views.cart,name='cart'),
]

urlpatterns =urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)