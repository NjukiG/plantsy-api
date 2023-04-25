from django.urls import path

from rest_framework.routers import SimpleRouter
# from .views import FlowersList, FlowersDetail, UserList, UserDetail  # new
from .views import UserViewSet, FlowersViewSet



router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", FlowersViewSet, basename="flowers")

urlpatterns = router.urls





# urlpatterns = [
#     path("users/", UserList.as_view()), # new
#     path("users/<int:pk>/", UserDetail.as_view()),  # new
#     path("<int:pk>/", FlowersDetail.as_view(), name="flowers_detail"),
#     path("", FlowersList.as_view(), name="flowers_list"),
# ]