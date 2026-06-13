from django.shortcuts import render, redirect
from catalog.models import Product, ContactInfo

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse_lazy, reverse

class HomeListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    paginate_by = 3


class ProductAddCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    template_name = 'product_add.html'
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    template_name = 'product_add.html'
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ContactView(View):

    def get(self, request):
        contacts_all = ContactInfo.objects.all()

        return render(request,'contacts.html',{'contacts': contacts_all})

    def post(self, request):
        ContactInfo.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            phone=request.POST.get('phone'),
            city=request.POST.get('city'),
            address=request.POST.get('address')
        )
        return redirect('catalog:contacts')
