from django.urls import include, path

urlpatterns = [
    path("v1/", include("apps.calculator.v1.urls")),
]
