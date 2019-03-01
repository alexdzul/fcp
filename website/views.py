from django.shortcuts import render
from django.views.generic import View


class Index(View):

    def get(self, request):
        return render(request, 'index.html')

def contact (request):
    ctx = {
        'email': None,
        'form': ContactForm()
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            mensaje = form.cleaned_data.get('mensaje')
            ctx[
                'mensaje'] = f'se obtuvieron los datos correctamente desde el servidor. Email {email}, Mensaje: {mensaje}'
        else:
            ctx['mensaje'] = 'Por favor, corrige tus errores'
            ctx['form'] = form
    return render(request, 'contact.html', ctx)
