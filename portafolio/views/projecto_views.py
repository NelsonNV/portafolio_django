from django.http import Http404
from core.views import BaseCreateView, BaseUpdateView, BaseDeleteView, BaseDetailView, BaseListView
from portafolio.models import Projecto
from portafolio.forms import ProjectoForm

class ProjectoListView(BaseListView):
    model = Projecto
    table_headers = ["Título", "Descripción", "Repositorio", "Imagen"]
    table_fields = ["title", "description", "repository", "image"]
    update_url_name = "proyectos_editar"
    delete_url_name = "proyectos_eliminar"
    create_url_name = "proyectos_crear"
    model_name_plural = "Proyectos"
    image_fields = ["image"]
    null_values = {"image": "(Sin imagen)", "repository": "No disponible"}

class ProjectoCreateView(BaseCreateView):
    model = Projecto
    form_class = ProjectoForm
    success_url = "/"
    title = "Crear Proyecto"

class ProjectoUpdateView(BaseUpdateView):
    model = Projecto
    form_class = ProjectoForm
    success_url = "/"
    title = "Editar Proyecto"

    def get_object(self, queryset=None):
        """
        Sobrescribe get_object para obtener el objeto por su ID.
        """
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("El proyecto solicitado no existe.")
        return obj

class ProjectoDeleteView(BaseDeleteView):
    model = Projecto
    success_url = "/"
    title = "Eliminar Proyecto"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("El proyecto solicitado no existe.")
        return obj

class ProjectoDetailView(BaseDetailView):
    model = Projecto
    title = "Detalle del Proyecto"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj:
            raise Http404("El proyecto solicitado no existe.")
        return obj

