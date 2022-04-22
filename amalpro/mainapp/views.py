from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .forms import *
from api.models import *

# Create your views here.

def dashboard(request):
    return render(request, "index.html")




def customers(request):
    form = CustomerForm()
    customers = Customer.objects.all()

    return render(request, "customer.html", {"form": form, "customers": customers})
    

def postCustomer(request):
    # request should be ajax and method should be POST.
    if request.accepts and request.method == "POST":
        # get the form data
        form = CustomerForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new Customer object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    if request.accepts and request.method == "PUT":
        # get the form data
        form = CustomerForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new Customer object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)