from django.http import Http404
from core.views import BaseCreateView, BaseUpdateView, BaseDeleteView, BaseDetailView
from portafolio.models import Estudios
from portafolio.forms import EstudiosForm

class EstudiosCreateView(BaseCreateView):
    model = Estudios
    form_class = EstudiosForm
    success_url = "/"
    title = "Crear Estudio"

class EstudiosUpdateView(BaseUpdateView):
    model = Estudios
    form_class = EstudiosForm
    success_url = "/"
    title = "Editar Estudio"

    def get_object(self, queryset=None):
        """
        Sobrescribe get_object para obtener el objeto por su ID.
        """
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("El registro del estudio solicitado no existe.")
        return obj

class EstudiosDeleteView(BaseDeleteView):
    model = Estudios
    success_url = "/"
    title = "Eliminar Estudio"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("El registro del estudio solicitado no existe.")
        return obj

class EstudiosDetailView(BaseDetailView):
    model = Estudios
    title = "Detalle del Estudio"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("El registro del estudio solicitado no existe.")
        return obj

