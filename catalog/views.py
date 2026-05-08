from django.shortcuts import render

def home(request):
    """ Контроллер для домашней страницы home.html """
    return render(request, 'home.html')


def contacts(request):
    """ Контроллер для страницы contacts.html """
    return render(request, 'contacts.html')