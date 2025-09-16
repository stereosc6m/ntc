from django.shortcuts import render

from .forms import RequestForm

def contacts(request):
    template_name = 'contacts/contacts.html'
    return render(request, template_name)

def create_request(request):
    template_name = 'contacts/create_request.html'
    form = RequestForm(
        request.POST or None,
    )
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, template_name, context)