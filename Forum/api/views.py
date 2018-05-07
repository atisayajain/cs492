from rest_framework import generics

from home.models import Post, Comment
from django.contrib.auth.models import User
from accounts.models import UserProfile
from .serializers import PostSerializer, CommentSerializer, ProfileSerializer


class PostRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = PostSerializer

	def get_queryset(self):
		return Post.objects.all()


class PostListView(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = PostSerializer

	def get_queryset(self):
		return Post.objects.all()


class CommentListView(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CommentSerializer

	def get_queryset(self):
		return Comment.objects.all()


class CommentRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = CommentSerializer

	def get_queryset(self):
		return Comment.objects.all()


class ProfileListView(generics.ListAPIView):
	lookup_field = 'user_id'
	serializer_class = ProfileSerializer

	def get_queryset(self):
		return UserProfile.objects.all()


class ProfileRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'user_id'
	serializer_class = ProfileSerializer

	def get_queryset(self):
		return UserProfile.objects.all()