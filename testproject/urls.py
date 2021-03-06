"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf.urls import url, include
import structlog
logger = structlog.get_logger(__name__)

logger.info("I am alive")

@api_view(['GET','POST'])
def hello_world(request):
    logger.info("Handling hello...")
    if request.method == 'POST':
            return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

urlpatterns = [
  url(r'^hello/$', hello_world),
]
