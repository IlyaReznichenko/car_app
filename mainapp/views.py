from django.shortcuts import render


def main_page(request):
    if request.POST:
        print(request.POST)
        print(request.FILES)
    return render(request, 'mainapp/index.html')