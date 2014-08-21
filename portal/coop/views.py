from django.shortcuts import render
from .forms import PartnerRegisterForm

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.POST:
        form = PartnerRegisterForm(request.POST)
        if form.is_valid(): 
            usuario = form.save()

            # Mandamos el mail para validar el email del usuario
            email_body = render_to_string('usuarios/registro_email_activacion.html', { 'usuario': usuario, 'base_url':settings.BASE_URL })
            email_subject = 'Uniq // Validacion de usuario'
            email = EmailMessage(email_subject, email_body, settings.EMAIL_HOST_USER, [usuario.email])
            email.content_subtype = "html"
            email.send()

            # No logre que funcione el redirect()
            return HttpResponseRedirect(reverse('usuarios.views.registro_gracias'))
    else:
        form = PartnerRegisterForm()

    return render(request, 'register.html', {'form': form})