from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.form import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .form import UserUpdateForm,ProfileUpdateForm


# Create your views here.
def register(request):
    # get the post method
    if request.method == 'POST':
        # show the form with post
        form = UserRegisterForm(request.POST)
        # check validation of the form
        if form.is_valid():
            # save the data
            form.save()
            # grab the username
            username = form.cleaned_data.get('username')
            # show the message you want
            # render or redirect to the next page
            messages.success(request,f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


# goto settings and LOGIN url for next page(LOGIN_URL = 'login')
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        # for saving the image use request.FILES
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request,f'Account has been Updated!')
            return redirect('user_profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {'u_form':u_form,'p_form':p_form,}

    return render(request,'users/profile.html',context)
