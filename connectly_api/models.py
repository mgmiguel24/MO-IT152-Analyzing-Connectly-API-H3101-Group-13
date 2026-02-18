# models.py
# -------------------------------------------------------
# WHAT IS THIS FILE?
# Think of this as the BLUEPRINT for your database tables.
# Just like a form has fields (name, age, email),
# each "model" here defines what a piece of data looks like.
#
# We have 3 models:
#   1. User     → a person using the app
#   2. Post     → something a user writes
#   3. Comment  → a reply to a post
# -------------------------------------------------------

from django.db import models


class User(models.Model):
    # A User has a username and an email address.
    # max_length = the maximum number of characters allowed.
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # unique=True means no two users can have the same email
    created_at = models.DateTimeField(auto_now_add=True)  # automatically saves when the user was created

    def __str__(self):
        # This controls what shows up when you print a User object.
        # Instead of seeing <User object>, you'll see the username.
        return self.username


class Post(models.Model):
    # A Post belongs to a User (the author).
    # ForeignKey means: "This post is linked to one User."
    # One User can have MANY Posts. (One-to-Many relationship)
    # on_delete=CASCADE means: if the user is deleted, all their posts are deleted too.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()  # TextField = long text (no character limit)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author.username}: {self.content[:30]}"
        # [:30] means show only the first 30 characters of the content


class Comment(models.Model):
    # A Comment belongs to BOTH a Post and a User (the commenter).
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on Post {self.post.id}"
