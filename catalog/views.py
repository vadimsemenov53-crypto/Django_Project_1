from django.shortcuts import render
from catalog.models import Product

def home(request):
    """ Контроллер для домашней страницы home.html """
    last_product = Product.objects.order_by('-created_at')[:3]

    print('Последние 3 товара:')
    for product in last_product:
        print(product.name)

    return render(request, 'home.html')


def contacts(request):
    """ Контроллер для страницы contacts.html """
    success = False

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        success = True

    return render(request, 'contacts.html', {
            'success': success
        })