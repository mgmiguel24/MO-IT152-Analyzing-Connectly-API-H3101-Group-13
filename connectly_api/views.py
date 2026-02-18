# views.py
# -------------------------------------------------------
# WHAT IS THIS FILE?
# Views are the BRAIN of your API.
# They receive a request, decide what to do, and send back a response.
#
# Think of it like a CUSTOMER SERVICE AGENT:
#   Customer says: "Give me all posts"   → Agent finds posts → returns them
#   Customer says: "Create a new post"   → Agent validates → saves it → confirms
#   Customer says: "Delete post #3"      → Agent checks it exists → deletes it
#
# We use Django REST Framework's ViewSets which give us
# all 4 CRUD operations automatically with very little code.
# -------------------------------------------------------

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    # ModelViewSet automatically gives you:
    #   GET    /api/users/      → list all users
    #   POST   /api/users/      → create a user
    #   GET    /api/users/{id}/ → get one user
    #   PUT    /api/users/{id}/ → update a user
    #   DELETE /api/users/{id}/ → delete a user
    # All 5 actions = full CRUD. Free with ModelViewSet!

    queryset = User.objects.all()
    # queryset = "which records do we work with?" → all users

    serializer_class = UserSerializer
    # serializer_class = "which translator do we use?" → UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        # We override 'create' to add a custom check:
        # Make sure the author exists before creating the post.
        # This is like a bouncer checking your ID before letting you in.

        author_id = request.data.get('author')
        if not User.objects.filter(id=author_id).exists():
            # If no user with that ID exists, reject the request
            return Response(
                {"error": f"User with id {author_id} does not exist."},
                status=status.HTTP_400_BAD_REQUEST
                # 400 = Bad Request (the client sent wrong/invalid data)
            )

        # If the author exists, proceed normally
        return super().create(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        # Same pattern: check that both the post AND the author exist
        # before allowing a comment to be created.

        post_id = request.data.get('post')
        author_id = request.data.get('author')

        if not Post.objects.filter(id=post_id).exists():
            return Response(
                {"error": f"Post with id {post_id} does not exist."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not User.objects.filter(id=author_id).exists():
            return Response(
                {"error": f"User with id {author_id} does not exist."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)
