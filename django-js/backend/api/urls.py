from django.urls import path
from .views import SampleAPI
from .views import Signup
from .views import Login
urlpatterns = [
    # path('sample/', SampleAPI.as_view(), name='sample_api'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/',Login.as_view(),name='login'),
]
