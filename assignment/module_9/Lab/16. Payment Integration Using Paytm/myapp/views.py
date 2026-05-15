from django.shortcuts import render, redirect
from myapp.models import *

def home(request):

    doctors = Doctor.objects.all()

    return render(request, 'home.html', {'doctors': doctors})


def payment_page(request, id):

    doctor = Doctor.objects.get(id=id)

    if request.method == "POST":

        name = request.POST['name']

        Payment.objects.create(
            doctor=doctor,
            customer_name=name,
            amount=doctor.fees,
            payment_status="Success",
            transaction_id="PAYTM123456"
        )

        return redirect('/success/')

    return render(request, 'payment.html', {'doctor': doctor})


def success(request):

    return render(request, 'payment_success.html')


def failed(request):

    return render(request, 'payment_failed.html')