# coding: utf-8
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Profile


def profile_detail_private(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.user.is_authenticated:
        return render(request, 'profiles/profile_detail.html', {
            'profile': profile,
        })




