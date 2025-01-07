from django.http import Http404
from core.views import BaseCreateView, BaseUpdateView, BaseDeleteView, BaseDetailView, BaseListView
from portafolio.models import SocialLink
from portafolio.forms import SocialLinkForm

class SocialLinkListView(BaseListView):
    model = SocialLink
    table_headers = ["Título", "URL", "SVG", "Activo"]
    table_fields = ["title", "url", "svg", "activo"]
    update_url_name = "enlaces_sociales_editar"
    delete_url_name = "enlaces_sociales_eliminar"
    model_name_plural = "Enlaces Sociales"

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

