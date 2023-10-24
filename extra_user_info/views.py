from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import UserExtraInfo
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from django.conf import settings
import json
import hashlib
import datetime


def signup_with_email(request):
    if request.method == 'POST':
        parsed_body = json.loads(request.body)
        receiver = parsed_body.get('to')
        # check if user is already exists
        try:
            user = UserExtraInfo.objects.get(email=receiver)
            if user:
                return JsonResponse({'success': False, 'message': 'User already exists'})
        except UserExtraInfo.DoesNotExist:
            # make signup_url
            token = hashlib.sha256(receiver.encode()).hexdigest()
            signup_url = request.get_host() + '/register?token=' + \
                token + '&email=' + receiver
            try:
                # send_mail(
                #     "Welcome " + receiver,
                #     signup_url,
                #     "noreply@example.com",
                #     [receiver],
                #     fail_silently=False,
                # )
                UserExtraInfo.objects.create(email=receiver, signup_url=token)
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'message': e})


def signup_with_token(request):
    if request.method == 'GET':
        signup_token = request.GET.get('token')
        user_email = request.GET.get('email')
        return render(request, 'signup.html', {'token': signup_token, 'email': user_email})
    elif request.method == 'POST':
        parsed_body = json.loads(request.body)
        token = parsed_body.get('token')
        email = parsed_body.get('email')
        password = parsed_body.get('password')
        # get user info from database
        try:
            user = UserExtraInfo.objects.get(email=email)
            if user.email:
                # compare token
                if user.signup_url == token:
                    # hash password and save userinfo
                    user.set_password(password)
                    user.last_login = datetime.datetime.now()
                    user.signup_url = None
                    user.save()
                    return JsonResponse({'success': True, 'redirectUrl': 'http://' + request.get_host()+'/'})
                else:
                    return JsonResponse({'success': False, 'message': 'Invalid token'})
        except UserExtraInfo.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Invalid email'})


def login_with_email(request):
    if request.method == 'POST':
        parsed_body = json.loads(request.body)
        email = parsed_body.get('email')
        password = parsed_body.get('password')
        # get user info from database
        try:
            user = UserExtraInfo.objects.get(email=email)
        except UserExtraInfo.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User does not exist'})
        # check password
        if not user.check_password(password):
            return JsonResponse({'success': False, 'message': 'Invalid password'})
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return JsonResponse({'success': True, 'redirectUrl': 'https://' + request.get_host()+'/'})
