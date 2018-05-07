from rest_framework import serializers
from home.models import Post, Comment
from accounts.models import UserProfile


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['pk', 'user', 'title', 'content', 'timestamp']
		read_only_fields = ['pk', 'user']


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['user', 'body', 'timestamp']


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ['user', 'roll', 'role', 'dept', 'year']

