from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Image, Profile, Comment
from django.contrib.auth.models import User
from .forms import SignupForm, ProfileForm, CommentForm, ImageForm
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from .email import activation_email
from django.contrib.auth import login
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
from .token import account_activation_token

# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.acquire_all_images()

    return render(request, 'home.html', {'images': images})


def registration(request):
    if request.user.is_authenticated():
        return redirect('index')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                email = form.cleaned_data.get('email')
                activation_email(user, current_site, email)
                return HttpResponse('Complete registration by confirming your email address')
        else:
            form = SignupForm()
        return render(request, 'registration/registration_form.html', {'form': form})


def confirm(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        return HttpResponse('Successful. Feel free to log into your account.')

    else:
        return HttpResponse('Invalid')


def profile(request, username):
    profile = User.objects.get(username=username)

    try:
        profile_details = Profile.acquire_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)

    image = Image.acquire_profile_image(profile.id)

    photos = Image.objects.filter(profile=profile)
    title = f'@{profile.username} Instagram profile'

    return render(request, 'profile/profile.html', {'title': title, 'profile': profile, 'profile-details': profile_details, 'image': image, 'photos': photos})


@login_required(login_url='/accounts/login/')
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile_edit')

    else:
        form = ProfileForm()

    return render(request, 'profile/profile_edit.html', {'form': form})


def profile_search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profile = Profile.profile_search(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message': message, 'profile': profile})
    else:
        message = 'Enter search term'
    return render(request, 'search.html', {'message': message})


@login_required(login_url='/accounts/login/')
def solo_image(request, image_id):
    image = Image.acquire_image_id(image_id)
    comment = Comment.acquire_image_comments(image_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = request.user
            comment.save()
            return redirect('solo_image', image_id=image_id)

    else:
       form = CommentForm()
    return render(request, 'pic.html', {'image': image, 'form': form, 'comment': comment})


@login_required(login_url='/accounts/login/')
def pic_upload(request):
    """
    Function for uploading of images to a profile once the user has been authenticated
    """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            upload.save()
            return redirect('profile', username=request.user)
    else:
        form = ImageForm()

    return render(request, 'profile/pic_upload.html', {'form': form})
