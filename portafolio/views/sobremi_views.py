from django.http import Http404, HttpResponseRedirect
from core.views import BaseCreateView, BaseUpdateView, BaseDeleteView, BaseDetailView
from portafolio.models import SobreMi
from portafolio.forms import SobreMiForm
from django.urls import reverse

class SobreMiCreateView(BaseCreateView):
    model = SobreMi
    form_class = SobreMiForm
    success_url = "/"
    title = "Crear Sobre Mí"

    def dispatch(self, request, *args, **kwargs):
        if SobreMi.objects.exists():
            return HttpResponseRedirect(reverse('sobre_mi_editar'))
        return super().dispatch(request, *args, **kwargs)


class SobreMiUpdateView(BaseUpdateView):
    model = SobreMi
    form_class = SobreMiForm
    success_url = '/'
    title = 'Editar Sobre Mí'

    def get_object(self, queryset=None):
        obj = SobreMi.objects.first()
        if not obj:
            raise Http404("No existe un registro en la tabla 'SobreMi'.")
        return obj

class SobreMiDeleteView(BaseDeleteView):
    model = SobreMi
    success_url = '/'
    title = 'Eliminar Sobre Mí'

    def get_object(self, queryset=None):
        obj = SobreMi.objects.first()
        if not obj:
            raise Http404("No existe un registro en la tabla 'SobreMi'.")
        return obj

class SobreMiDetailView(BaseDetailView):
    model = SobreMi
    title = 'Detalle Sobre Mí'

    def get_object(self, queryset=None):
        obj = SobreMi.objects.first()
        if not obj:
            raise Http404("No existe un registro en la tabla 'SobreMi'.")
        return obj
