from django.urls import path
from .views import *

from rest_framework.routers import SimpleRouter
 

router = SimpleRouter()
router.register('details',ProductView,basename="Product-details")
router.register('seller',ProductView,basename="Product-seller")

urlpatterns = [
    path('feed/',PersonalizedFeedView.as_view())
]+router.urls
