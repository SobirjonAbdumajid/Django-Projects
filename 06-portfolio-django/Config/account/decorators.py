from django.shortcuts import redirect

def login_required(my_view):
    def decorator(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return my_view(request, *args, **kwargs)
    return decorator