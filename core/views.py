from django.shortcuts import render


def frontpage(request):
    template = "core/frontpage.html"
    return render(request, template)

def privacy(request):
    template = "core/privacy.html"
    return render(request, template)

def terms_of_service(request):
    template = "core/terms.html"
    return render(request, template)

def plans(request):
    template = "core/plans.html"
    return render(request, template)
