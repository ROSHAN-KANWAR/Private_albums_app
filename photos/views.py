from django.shortcuts import render, redirect
from .models import Category, Photo
from .forms import Registerform,Logonform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

##gallery view
@login_required(login_url='login')
def Gallery(request):
    user=request.user
    category = request.GET.get('category')
    if category == None:
        photo = Photo.objects.filter(category__user=user)
    else:
        photo = Photo.objects.filter(category__category=category,category__user=user)
    category = Category.objects.filter(user=user)

    context = {'category': category, 'photo': photo}
    return render(request, 'photos/gallery.html', context)


##View photos
@login_required(login_url='login')
def Viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})


##add photo
@login_required(login_url='login')
def Addphoto(request):
    user=request.user
    category = user.category_set.all()

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(user=user,category=data['category_new'])
        else:
            category = None
        photo = Photo.objects.create(
            category=category,
            dec=data['dec'],
            image=image,
        )
        messages.info(request,"Successfully Add Photo")
        return redirect('gallery')
    return render(request, 'photos/add.html', {'category': category})


##login page
def Loginuser(request):
    page = "login"
    if request.method == 'POST':
        form = Logonform(request=request, data=request.POST)
        if form.is_valid():
            uname1 = form.cleaned_data['username']
            upass1 = form.cleaned_data['password']
            user = authenticate(username=uname1, password=upass1)
            if user is not None:
                login(request, user)
                messages.info(request, 'Login Successfully ! Now enjoy app ')
                return redirect('gallery')
    else:
        form = Logonform()
    return render(request, 'photos/login.html', {'page': page,'form':form})


##logout
def Logoutuser(request):
    logout(request)
    messages.success(request, "Successfull Logout !!")
    return redirect('login')


##register
def Register(request):
    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user = authenticate(request, username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                messages.success(request, "Successfull login !! Now Login and Enjoy the app")
                return redirect('gallery')
    else:
        form = Registerform()
    return render(request, 'photos/register.html', {'form': form})
