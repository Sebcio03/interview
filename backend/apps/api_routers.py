from django.urls import include, path

urlpatterns = [
    path("calculator/", include("apps.calculator.urls")),
]
