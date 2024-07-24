from django.shortcuts import render,redirect


def admin_only(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_staff:
            return view_function(request,*args,**kwargs)
        else:
            return redirect('/')
    return wrapper_function    

        