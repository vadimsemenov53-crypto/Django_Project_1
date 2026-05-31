from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Product, ContactInfo, Category
from django.core.paginator import Paginator

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView

class HomeListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    paginate_by = 3


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
    category = Category.objects.all()
    context = {
        'category': category,
    }

    if request.method == 'POST':
        category_id = request.POST.get('category')
        category_obj = Category.objects.get(pk=category_id)

        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
            category=category_obj,
            price=request.POST.get('price')
        )
        return redirect('catalog:home')

    return render(request,'product_add.html', context=context)

