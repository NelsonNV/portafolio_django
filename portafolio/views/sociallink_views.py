from django.http import Http404
from core.views import BaseCreateView, BaseUpdateView, BaseDeleteView, BaseDetailView
from portafolio.models import SocialLink
from portafolio.forms import SocialLinkForm

class SocialLinkCreateView(BaseCreateView):
    model = SocialLink
    form_class = SocialLinkForm
    success_url = "/"
    title = "Crear Enlace Social"

class SocialLinkUpdateView(BaseUpdateView):
    model = SocialLink
    form_class = SocialLinkForm
    success_url = "/"
    title = "Editar Enlace Social"

    def get_object(self, queryset=None):
        """
        Sobrescribe get_object para obtener el objeto por su ID.
        """
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("El enlace social solicitado no existe.")
        return obj

class SocialLinkDeleteView(BaseDeleteView):
    model = SocialLink
    success_url = "/"
    title = "Eliminar Enlace Social"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("El enlace social solicitado no existe.")
        return obj

class SocialLinkDetailView(BaseDetailView):
    model = SocialLink
    title = "Detalle del Enlace Social"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("El enlace social solicitado no existe.")
        return obj

