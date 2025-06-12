# Uncomment the required imports before adding the code

# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
# from .populate import initiate
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
async def login_user(request):
    if request.method == "POST":
        # Read the body asynchronously
        body = await request.body
        data = json.loads(body)

        username = data.get('userName')
        password = data.get('password')

        # Authenticate asynchronously
        user = await sync_to_async(authenticate)(username=username, password=password)
        response_data = {"userName": username}

        if user is not None:
            # Login asynchronously
            await sync_to_async(login)(request, user)
            response_data["status"] = "Authenticated"
        else:
            response_data["status"] = "Invalid credentials"

        return JsonResponse(response_data)

    return JsonResponse({"error": "Only POST method is allowed"}, status=405)

# Create a `logout_request` view to handle sign out request
@csrf_exempt
async def logout_user(request):
    if request.method == "POST":
        await sync_to_async(logout)(request)
        return JsonResponse({"status": "Logged out"})
    return JsonResponse({"error": "Only POST method is allowed"}, status=405)
# ...

# Create a `registration` view to handle sign up request
# @csrf_exempt
# def registration(request):
# ...

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...
