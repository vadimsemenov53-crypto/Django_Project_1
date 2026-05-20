from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Product, ContactInfo

def home(request):
    """ Контроллер для домашней страницы home.html """
    last_product = Product.objects.order_by('-created_at')[:3]

    print('Последние 3 товара:')
    for product in last_product:
        print(product.name)

    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'home.html', context=context)


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


def product_detail(request, pk):
    """ Контроллер для детального отображения товара product_detail.html. """
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product,}

    return render(request, 'product_detail.html', context=context)


def product_add(request):
    """ Контроллер для станицы добавления нового товара. """
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            image=request.POST.get('image'),
            category=request.POST.get('category'),
            price=request.POST.get('address')
        )
        return redirect('catalog:product_add')

    return render(request,'product_add.html',)

