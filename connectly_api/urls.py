# connectly_api/urls.py
# -------------------------------------------------------
# WHAT IS THIS FILE?
# This is the ADDRESS BOOK of your API.
# It maps URLs to views — like a directory:
#
#   /api/users/    → UserViewSet (handles all user requests)
#   /api/posts/    → PostViewSet (handles all post requests)
#   /api/comments/ → CommentViewSet (handles all comment requests)
#
# The Router does this automatically. You register a viewset
# and it creates ALL the URL patterns for you.
# -------------------------------------------------------

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, CommentViewSet

# Create a router — think of it as a smart URL manager
router = DefaultRouter()

# Register our viewsets with the router
# 'users' = the URL prefix   |   UserViewSet = the view to use
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# The router auto-generates these URLs:
#   GET    /api/users/        → list all users
#   POST   /api/users/        → create user
#   GET    /api/users/{id}/   → get one user
#   PUT    /api/users/{id}/   → update user
#   DELETE /api/users/{id}/   → delete user
# (Same pattern for posts and comments)

urlpatterns = [
    path('', include(router.urls)),
]
