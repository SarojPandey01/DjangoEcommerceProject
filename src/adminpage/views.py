from django.shortcuts import render

# Create your views here.
def admin_page(request):
    return render(request,'admins/admin.html')

