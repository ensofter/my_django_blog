from django.urls import path
from .views import (
    MainView, PostDetailView, SignUpView, SignInView, FeedBackView, SuccessView, SearchResultsView, TagView
)
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout',),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('tag/<slug:slug>/', TagView.as_view(), name="tag"),
]