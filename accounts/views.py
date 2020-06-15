from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer

from movies.models import Review
from movies.serializers import ReviewSerializer


User = get_user_model()


@api_view(['GET'])
def profile(request, username):
    user = User.objects.get(username=username)
    serializer = UserSerializer(user)
    review = Review.objects.filter(reviewer__pk=user.pk)
    serializer_reviews = ReviewSerializer(review, many=True)
    context = {
        'profile': serializer.data,
        'reviews': serializer_reviews.data,
    }
    return Response(context)