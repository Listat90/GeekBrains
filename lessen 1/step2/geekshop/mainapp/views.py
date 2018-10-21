from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/index.html')

def product (request):
    return render(request, 'mainapp/product.html' )

def contact (request):
    return render(request, 'mainapp/contact')

# Create your views here.
