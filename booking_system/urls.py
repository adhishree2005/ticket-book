from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='shows/'), name='home'),

 
    path('accounts/', include('accounts.urls', namespace='accounts')),


    path('shows/', include('tickets.urls', namespace='tickets')),
]
