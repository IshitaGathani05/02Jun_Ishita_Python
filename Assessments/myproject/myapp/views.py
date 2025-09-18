from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, ProfileForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import *
import stripe
from django.conf import settings
from django.shortcuts import redirect

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.

def home(request):
    courses = Course.objects.filter(published=True)[:12]
    return render(request, 'home.html', {'courses': courses})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myapp:home')
    else:
        form = SignUpForm()
    return render(request, 'myapp/signup.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('myapp:profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'myapp/profile.html', {'form': form})

def course_list(request):
    qs = Course.objects.filter(published=True)
    return render(request, 'courses/list.html', {'courses': qs})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, published=True)
    enrolled = request.user.is_authenticated and Enrollment.objects.filter(student=request.user, course=course).exists()
    return render(request, 'courses/detail.html', {'course': course, 'enrolled': enrolled})

@login_required
def enroll(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(student=request.user, course=course)
    # For demo: mark paid=False and redirect to a "checkout" page or success
    return redirect(reverse('courses:detail', args=[slug]))



stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request, slug):
    # Demo: create a Stripe Checkout session
    course = get_object_or_404(Course, slug=slug)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'inr',
                'unit_amount': int(course.fee * 100),
                'product_data': {'name': course.title},
            },
            'quantity': 1
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/courses/') + '?paid=1',
        cancel_url=request.build_absolute_uri('/courses/') + '?paid=0',
    )
    return redirect(session.url, code=303)

import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'inr',
                'product_data': {'name': 'Test Course'},
                'unit_amount': 50000,  # 500 INR
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/success',
        cancel_url='http://127.0.0.1:8000/cancel',
    )
    return redirect(session.url, code=303)