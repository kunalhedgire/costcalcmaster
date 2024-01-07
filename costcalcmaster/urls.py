"""
URL configuration for costcalcmaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cost_calculator.views import AddItemsView, SaveItemsView, SummaryView, ShowAddItemsView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', add_items, name='add_items'),
#     path('save-items/', save_items, name='save_items'),
#     path('summary/', summary, name='summary'),
#     path('show-add-items/', show_add_items, name='show_add_items'),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-items/', AddItemsView.as_view(), name='add_items'),
    path('save-items/', SaveItemsView.as_view(), name='save_items'),
    path('summary/', SummaryView.as_view(), name='summary'),
    path('show-add-items/', ShowAddItemsView.as_view(), name='show_add_items'),
]

urlpatterns += staticfiles_urlpatterns()
