from django.http import Http404
from core.views import BaseCreateView, BaseUpdateView, BaseDeleteView, BaseDetailView, BaseListView
from portafolio.models import Estudios
from portafolio.forms import EstudiosForm
class EstudiosListView(BaseListView):
    model = Estudios
    table_headers = ["Institución", "Título", "Descripción", "Inicio", "Fin", "Certificado", "Mostrar"]
    table_fields = ["institucion", "titulo", "description", "inicio", "fin", "certificado", "mostrar"]
    update_url_name = "estudios_editar"
    create_url_name ="estudios_crear"
    delete_url_name = "estudios_eliminar"
    model_name_plural = "Estudios"
    image_fields = ["certificado"]
    null_values = {"certificado": "(Sin certificado)"}
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

