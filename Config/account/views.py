from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser, CodeConfirmation
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password, check_password
from .decorators import login_required
from helpers import sms_send, random_code

# Create your views here.


# def code_confirmation(request):
#     email = request.POST.get('email')
#     code = request.POST.get('code')
#     user = CustomUser.objects.filter(email=email).first()
#     if user:
#         obj = CodeConfirmation.objects.filter(user=user).first()
#         if obj:
#             user.is_active = True
#             user.save()
#             login(request, user)
#             obj.delete()
#             return redirect('home')
#         return HttpResponse('<h1>Something went wrong</h1>')
#     print(code)
#     return render(
#         request=request,
#         template_name='auth/code_confirmation.html'
#     )

def code_confirmation(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        code = request.POST.get('code')
        user = CustomUser.objects.filter(email=email).first()

        if user:
            obj = CodeConfirmation.objects.filter(user=user, code=code).first()
            if obj:
                user.is_active = True
                user.save()
                login(request, user)
                obj.delete()
                return redirect('home')
            else:
                return HttpResponse('<h1>Invalid code</h1>')
        else:
            return HttpResponse('<h1>User does not exist</h1>')

    return render(
        request=request,
        template_name='auth/code_confirmation.html'
    )
@login_required
def log_in(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request=request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('<h1>Invalid Credentials</h1>')
    return render(
        request=request,
        template_name='auth/login.html'
    )

# @login_required
# def register(request):
#     if request.method == 'POST':
#         print(request.POST)
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#         # print(first_name, last_name, email, password, confirm_password)
#         x_user = CustomUser.objects.filter(email=email).first()
#         if x_user:
#             return HttpResponse('<h1>Email already registered</h1>')
#         elif password != confirm_password:
#             return HttpResponse('<h1>Passwords do not match</h1>')
#         else:
#             user = CustomUser.objects.create_user(
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#                 password=make_password(password),
#             )
#             code = random_code.generate_code()
#             sms_send.send_email(email, code)
#             CodeConfirmation.objects.create(
#                 user=user,
#                 code=code
#             )
#             return redirect('code_confirmation')
#     return render(
#         request=request,
#         template_name='auth/register.html'
#     )
# @login_required
# def register(request):
#     if request.method == 'POST':
#         print(request.POST)
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#         x_user = CustomUser.objects.filter(email=email).first()
#         if x_user:
#             return HttpResponse('<h1>Email already registered</h1>')
#         elif password != confirm_password:
#             return HttpResponse('<h1>Passwords do not match</h1>')
#         else:
#             user = CustomUser.objects.create_user(
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#                 password=make_password(password),
#             )
#             code = random_code.generate_code()
#             sms_send.send_email(email, code)
#             CodeConfirmation.objects.create(
#                 user=user,
#                 code=code
#             )
#             return redirect('code_confirmation')
#     return render(
#         request=request,
#         template_name='auth/register.html'
#     )

# @login_required
# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#
#         if CustomUser.objects.filter(email=email).exists():
#             return HttpResponse('<h1>Email already registered</h1>')
#         elif password != confirm_password:
#             return HttpResponse('<h1>Passwords do not match</h1>')
#         else:
#             user = CustomUser.objects.create_user(
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#                 password=make_password(password),
#             )
#             code = random_code.generate_code()
#             sms_send.send_email(email, code)
#             CodeConfirmation.objects.create(
#                 user=user,
#                 code=code
#             )
#             return redirect('code_confirmation')
#     return render(
#         request=request,
#         template_name='auth/register.html'
#     )




@login_required
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse('<h1>Email already registered</h1>')
        elif password != confirm_password:
            return HttpResponse('<h1>Passwords do not match</h1>')
        else:
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=make_password(password),
            )
            code = random_code.generate_code()
            sms_send.send_email(email, code)
            CodeConfirmation.objects.create(
                user=user,
                code=code
            )
            return redirect('code_confirmation')
    return render(
        request=request,
        template_name='auth/register.html'
    )

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    # else:
    #     return redirect('world')


