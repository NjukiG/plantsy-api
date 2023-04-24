from django.urls import path

from .views import FlowesList, FLowersDetail


urlpatterns = [
    path("<int:pk>/", FlowersDetail.as_view(), name="flowers_detail"),
    path("", FlowersList.as_view(), name="flowers_list"),
]