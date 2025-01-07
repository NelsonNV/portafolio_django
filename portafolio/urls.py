from django.urls import path
from core.views import IndexView
from portafolio.views.experiencia_views import (
    ExperienciaCreateView, ExperienciaUpdateView, ExperienciaDeleteView, ExperienciaDetailView, ExperienciaListView
)
from portafolio.views.sobremi_views import (
    SobreMiCreateView, SobreMiUpdateView, SobreMiDeleteView, SobreMiDetailView
)
from portafolio.views.sociallink_views import (
    SocialLinkCreateView, SocialLinkUpdateView, SocialLinkDeleteView, SocialLinkDetailView, SocialLinkListView
)
from portafolio.views.projecto_views import (
    ProjectoCreateView, ProjectoUpdateView, ProjectoDeleteView, ProjectoDetailView, ProjectoListView
)
from portafolio.views.estudios_views import (
    EstudiosCreateView, EstudiosUpdateView, EstudiosDeleteView, EstudiosDetailView, EstudiosListView
)

urlpatterns = [
    # Página principal
    path("", IndexView.as_view(), name="index"),
    # Sobre Mí
    path("sobre-mi/crear/", SobreMiCreateView.as_view(), name="sobre_mi_crear"),
    path("sobre-mi/editar/", SobreMiUpdateView.as_view(), name="sobre_mi_editar"),
    path("sobre-mi/eliminar/", SobreMiDeleteView.as_view(), name="sobre_mi_eliminar"),
    path("sobre-mi/detalle/", SobreMiDetailView.as_view(), name="sobre_mi_detalle"),
    # Enlaces Sociales
    path("enlaces-sociales/crear/", SocialLinkCreateView.as_view(), name="enlaces_sociales_crear"),
    path("enlaces-sociales/editar/<int:pk>/", SocialLinkUpdateView.as_view(), name="enlaces_sociales_editar"),
    path("enlaces-sociales/eliminar/<int:pk>/", SocialLinkDeleteView.as_view(), name="enlaces_sociales_eliminar"),
    path("enlaces-sociales/detalle/<int:pk>/", SocialLinkDetailView.as_view(), name="enlaces_sociales_detalle"),
    path("enlaces-sociales/lista/", SocialLinkListView.as_view(), name="enlaces_sociales_lista"),

    # Proyectos
    path("proyectos/crear/", ProjectoCreateView.as_view(), name="proyectos_crear"),
    path("proyectos/editar/<int:pk>/", ProjectoUpdateView.as_view(), name="proyectos_editar"),
    path("proyectos/eliminar/<int:pk>/", ProjectoDeleteView.as_view(), name="proyectos_eliminar"),
    path("proyectos/detalle/<int:pk>/", ProjectoDetailView.as_view(), name="proyectos_detalle"),
    path("proyectos/lista/", ProjectoListView.as_view(), name="proyectos_lista"),

    # Experiencias
    path("experiencias/crear/", ExperienciaCreateView.as_view(), name="experiencias_crear"),
    path("experiencias/editar/<int:pk>/", ExperienciaUpdateView.as_view(), name="experiencias_editar"),
    path("experiencias/eliminar/<int:pk>/", ExperienciaDeleteView.as_view(), name="experiencias_eliminar"),
    path("experiencias/detalle/<int:pk>/", ExperienciaDetailView.as_view(), name="experiencias_detalle"),
    path("experiencias/lista/", ExperienciaListView.as_view(), name="experiencias_lista"),

    # Estudios
    path("estudios/crear/", EstudiosCreateView.as_view(), name="estudios_crear"),
    path("estudios/editar/<int:pk>/", EstudiosUpdateView.as_view(), name="estudios_editar"),
    path("estudios/eliminar/<int:pk>/", EstudiosDeleteView.as_view(), name="estudios_eliminar"),
    path("estudios/detalle/<int:pk>/", EstudiosDetailView.as_view(), name="estudios_detalle"),
    path("estudios/lista/", EstudiosListView.as_view(), name="estudios_lista"),
]
