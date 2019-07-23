from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'members/index.html', {})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'members/register.html', {'form': form})

def members(request):
    member_model = Member.objects.all()
    context = {'members': member_model}
    return render(request, 'members/members.html', context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = form = ContactForm()
    context = {'form': form}
    return render(request, 'members/contact.html', context)

def about(request):
    return render(request, 'members/about.html', {})

def user_url(request, nickname):
    user = get_object_or_404(Member, nickname__iexact = nickname)
    context = {'users': user}
    return render(request, 'members/user_profile.html', context)

@login_required
def profile(request):
    return render(request, 'members/profile.html', {})
