from django.shortcuts import render, redirect, HttpResponse
from django import template

from .models import ParcelList,DriverList
from .utils import decide_compartment
from .forms import UserForm


register = template.Library()
# Create your views here.

def index(request):
    parcels = ParcelList.objects.all()
    context = {
        'parcels': parcels
    }
    return render(request, 'index.html', context)

def pick_up_point(request):
    drivers = DriverList.objects.all()
    context = {
        'drivers': drivers
    }
    return render(request,'pick_up_point.html',context)

def sort(request):
    parcels = ParcelList.objects.all()
    context = {
        'parcels': parcels
    }
    return render(request,'sort.html',context)

def create(request):
    print(request.POST)
    tracking_no = request.GET['tracking_no']
    postcode = request.GET['postcode']
    address = request.GET['address']
    compartment,destination = decide_compartment(int(postcode))
    parcel_details = ParcelList(tracking_no=tracking_no, postcode=postcode, address=address, compartment=compartment, destination=destination)
    parcel_details.save()
    return redirect('/')

def create_driver(request):
    print(request.POST)
    zone = request.GET['zone']
    min_postcode = request.GET['min_postcode']
    max_postcode = request.GET['max_postcode']
    compartment = request.GET['compartment']
    driver_details = DriverList(zone=zone, min_postcode=min_postcode, max_postcode=max_postcode, compartment=compartment)
    driver_details.save()
    return redirect('/pick_up_point')

def add_parcel(request):
    return render(request, 'add_parcel.html')

def add_driver(request):
    context = {}
    return render(request,'add_driver.html',context)

def delete(request, id):
    parcels = ParcelList.objects.get(pk=id)
    parcels.delete()
    return redirect('/')

def delete_driver(request, id):
    drivers = DriverList.objects.get(pk=id)
    drivers.delete()
    return redirect('/pick_up_point')

def edit(request, id):
    parcels = ParcelList.objects.get(pk=id)
    context = {
        'parcels': parcels
    }
    return render(request, 'edit.html', context)

def edit_driver(request, id):
    drivers = DriverList.objects.get(pk=id)
    context = {
        'drivers': drivers
    }
    return render(request, 'edit_driver.html', context)

def edit_sort(request, id):
    parcels = ParcelList.objects.get(pk=id)
    context = {
        'parcels': parcels
    }
    return render(request, 'edit_sort.html', context)

def update(request, id):
    parcels = ParcelList.objects.get(pk=id)
    parcels.tracking_no = request.GET['tracking_no']
    parcels.postcode = request.GET['postcode']
    parcels.address = request.GET['address']
    parcels.save()
    return redirect('/')

def update_driver(request, id):
    drivers = DriverList.objects.get(pk=id)
    drivers.zone = request.GET['zone']
    drivers.min_postcode = request.GET['min_postcode']
    drivers.max_postcode = request.GET['max_postcode']
    drivers.compartment = request.GET['compartment']
    drivers.save()
    return redirect('/pick_up_point')

def update_sort(request, id):
    parcels = ParcelList.objects.get(pk=id)
    parcels.tracking_no = request.GET['tracking_no']
    parcels.compartment = request.GET['compartment']
    parcels.destination = request.GET['destination']
    parcels.save()
    return redirect('/sort.html')

def query(request):
    submitbutton= request.POST.get("submit")

    tracking_no = ''
    compartment_answer = ''
    destination_answer = ''
    postcode = ''
    address = ''

    form= UserForm(request.POST or None)
    if form.is_valid():
        tracking_no= form.cleaned_data.get("tracking_no")

        parcels = ParcelList.objects.all()
        answer = ParcelList.objects.filter(tracking_no = tracking_no)
        compartment_answer = answer.values_list('compartment', flat=True)[0]
        destination_answer = answer.values_list('destination', flat=True)[0]
        postcode = answer.values_list('postcode', flat=True)[0]
        address = answer.values_list('address', flat=True)[0]
    context= {'form': form, 'tracking_no': tracking_no,
              'submitbutton': submitbutton,'compartment_answer': compartment_answer,
              'destination_answer' : destination_answer,'postcode':postcode,'address':address}

    return render(request, 'query.html', context)
