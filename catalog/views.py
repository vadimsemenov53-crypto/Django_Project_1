from django.shortcuts import render, redirect
from catalog.models import Product, ContactInfo

def home(request):
    """ Контроллер для домашней страницы home.html """
    last_product = Product.objects.order_by('-created_at')[:3]

    print('Последние 3 товара:')
    for product in last_product:
        print(product.name)

    return render(request, 'home.html')


def contacts(request):
    """ Контроллер для страницы contacts.html """

    if request.method == 'POST':
        ContactInfo.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            phone=request.POST.get('phone'),
            city=request.POST.get('city'),
            address=request.POST.get('address')
        )
        return redirect('catalog:contacts')

    contacts_all = ContactInfo.objects.all()

    return render(
        request,
        'contacts.html',
        {'contacts': contacts_all
         })