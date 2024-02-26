from apps.calculator.v1.views import CalculateAPIView
from django.urls import path

urlpatterns = [
    path("calculate/", CalculateAPIView.as_view()),
]
