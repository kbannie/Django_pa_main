from django.shortcuts import render

def landing(request):
    return render(
        request,
        'single_pages/lading.html',
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html',
    )