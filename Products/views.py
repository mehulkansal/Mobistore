from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from Products.models import Product1, shop  # , cart,  customer
# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    if request.user.is_authenticated:
        context = Product1.objects.all()
        return render(request, "home.html", {'context': context})
    else:
        context = Product1.objects.all()
        return render(request, "home.html", {'context': context})
       # return redirect("signup")


def product(request):
    print(request.user)

    # try:

    #prod = Product1.objects.filter(Name='')
   # except Exception as e:
    #    print(e)
    return render(request, "product.html")


def cart(request):
    if request.user.is_authenticated:
        return render(request, "cart.html")
    else:
        return redirect("signin.html")


def contact(request):
    return render(request, "contact.html")


# def product(request):
    return render(request, "product.html")


def sign_in(request):
    return redirect("")


def sign_up(request, *args, **kwargs):
    return render(request, "sign_up.html")


def checkout(request):
    return redirect("")


def dealer_signup(request):
    return redirect("")
