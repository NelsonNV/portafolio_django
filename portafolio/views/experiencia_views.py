
from django.http import Http404
from core.views import BaseCreateView, BaseUpdateView, BaseDeleteView, BaseDetailView
from portafolio.models import Experiencia
from portafolio.forms import ExperienciaForm

class ExperienciaCreateView(BaseCreateView):
    model = Experiencia
    form_class = ExperienciaForm
    success_url = "/"
    title = "Crear Experiencia"

class ExperienciaUpdateView(BaseUpdateView):
    model = Experiencia
    form_class = ExperienciaForm
    success_url = "/"
    title = "Editar Experiencia"

    def get_object(self, queryset=None):
        """
        Sobrescribe get_object para obtener el objeto por su ID.
        """
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("La experiencia solicitada no existe.")
        return obj

class ExperienciaDeleteView(BaseDeleteView):
    model = Experiencia
    success_url = "/"
    title = "Eliminar Experiencia"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("La experiencia solicitada no existe.")
        return obj

class ExperienciaDetailView(BaseDetailView):
    model = Experiencia
    title = "Detalle de la Experiencia"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("La experiencia solicitada no existe.")
        return obj
