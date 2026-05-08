from django.shortcuts import render

def home(request):
    """ Контроллер для домашней страницы home.html """
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