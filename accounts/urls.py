from django.urls import path

# from .views import AccountSignUpView, AccountSignInView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # path("signup/", AccountSignUpView.as_view(), name="signup"),
    # path("signin/", AccountSignInView.as_view(), name="signin"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
