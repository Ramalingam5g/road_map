"""road_map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from .views import RoadDetail,RoadList,RoadTypeView,RoadPropertyView

#import pdb;pdb.set_trace()
urlpatterns = [
    #path('get/', RoadList.as_view(),name='get'),
    path('roadtype/',RoadTypeView.as_view()),
    path('attribute/',RoadPropertyView.as_view()),
    path('update/<int:id>',RoadList.as_view(),name='put'),
    path('delete/<int:id>',RoadList.as_view(),name='delete'),
    path('', RoadList.as_view()),
    #path('get/<int:pk>/', views.RoadDetail.as_view()),
    # path('post/',RoadDetail.as_view(),name='post'),
    # path('get/',RoadDetail.as_view(),name='get'),
    # path('get_object/<int:pk>',RoadDetail.as_view(),name='get_object'),
    # path('put/<int:id>',RoadDetail.as_view(),name='put'),
    # path('delete/<int:id>',RoadDetail.as_view(),name='delete')
    
]