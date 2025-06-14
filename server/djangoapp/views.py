# Uncomment the required imports before adding the code

# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime


from .populate import initiate
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
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"userName": username, "status": "Authenticated"})
        else:
            return JsonResponse({"userName": username, "status": "Invalid credentials"})
    return JsonResponse({"error": "Only POST method is allowed"}, status=405)

# Create a `logout_request` view to handle sign out request
@csrf_exempt
def logout_request(request):
    logout(request) # Terminate user session
    data = {"userName":""} # Return empty username
    return JsonResponse(data)

# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    context = {}

    # Load JSON data from the request body
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    email_exist = False
    try:
        # Check if user already exists
        User.objects.get(username=username)
        username_exist = True
    except:
        # If not, simply log this is a new user
        logger.debug("{} is new user".format(username))

    # If it is a new user
    if not username_exist:
        # Create user in auth_user table
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password, email=email)
        # Login the user and redirect to list page
        login(request, user)
        data = {"userName":username,"status":"Authenticated"}
        return JsonResponse(data)
    else :
        data = {"userName":username,"error":"Already Registered"}
        return JsonResponse(data)
# ...

@csrf_exempt
def get_car_list(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)

    # Check if database is empty and populate if needed
    if CarMake.objects.count() == 0:
        initiate()

    # Get pagination parameters
    try:
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 30))
    except ValueError:
        return JsonResponse({'error': 'Offset and limit must be integers'}, status=400)

    # Fetch all car models with related makes
    all_cars = list(CarModel.objects.select_related('car_make').all())
    random.shuffle(all_cars)  # Randomize the list

    # Paginate
    paginated_cars = all_cars[offset:offset+limit]

    if not paginated_cars:
        return JsonResponse({'message': 'End of List'}, status=200)

    car_data = [{
        'id': car.id,
        'name': car.name,
        'make': car.car_make.name,
        'type': car.type,
        'year': car.year,
        'fuel_efficiency': car.fuel_efficiency,
        'price': float(car.price),
        'image_url': car.image_url
    } for car in paginated_cars]

    return JsonResponse({'CarModels': car_data}, status=200)

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
