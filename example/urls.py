"""
URL configuration for example project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from graphene_django.views import GraphQLView
from rest_framework import routers
from example.quickstart import views
from django.views.decorators.csrf import csrf_exempt
from django.urls import path, include
from rest import views as views2
from rest.views import TakeList3
from api.views import UserViews, ProductViews, OrderViews
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'TakeList3', TakeList3, basename='TakeList3')
router.register(r'UserViews',UserViews, basename='UserViews')
router.register(r'Product',ProductViews, basename='ProductViews')
router.register(r'Order',OrderViews, basename='OrderViews')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')) 
]
