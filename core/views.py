from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from portafolio.models import SobreMi, SocialLink, Projecto, Experiencia
from django.urls import reverse_lazy



class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sobremi"] = SobreMi.objects.first()
        context["social_links"] = SocialLink.objects.filter(activo=True)
        context["projects"] = Projecto.objects.all()
        context["experiencias"] = Experiencia.objects.filter(mostrar=True)
        return context


class BaseCreateView(CreateView):
    template_name = "formulario.html"
    title = "Crear Registro"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view"] = self
        return context


class BaseUpdateView(UpdateView):
    template_name = "formulario.html"
    title = "Editar Registro"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view"] = self
        return context


class BaseDetailView(DetailView):
    template_name = "detalle.html"
    title = "Detalle del Registro"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view"] = self
        return context

class BaseDeleteView(DeleteView):
    template_name = "confirm_delete.html"
    title = "Eliminar Registro"
    success_url = reverse_lazy('index')  # Redirige a la página principal por defecto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view"] = self
        return context
