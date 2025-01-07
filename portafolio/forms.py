from django import forms
from portafolio.models import SobreMi, SocialLink, Projecto, Experiencia, Estudios


class BaseForm(forms.ModelForm):
    """
    Formulario base para extender funcionalidades comunes.
    """

    class Meta:
        abstract = True

    def add_common_styles(self):
        """
        Método para agregar clases CSS comunes a todos los campos.
        """
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control",
                }
            )


class SobreMiForm(BaseForm):
    class Meta:
        model = SobreMi
        fields = ["nombre", "apellido", "descripcion", "perfil", "fondo"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_common_styles()


class SocialLinkForm(BaseForm):
    class Meta:
        model = SocialLink
        fields = ["title", "url", "svg", "activo"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_common_styles()


class ProjectoForm(BaseForm):
    class Meta:
        model = Projecto
        fields = [
            "title",
            "description",
            "repository",
            "pagina",
            "image",
            "inicio",
            "fin",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_common_styles()


class ExperienciaForm(BaseForm):
    class Meta:
        model = Experiencia
        fields = ["empresa", "cargo", "description", "url", "inicio", "fin", "mostrar"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_common_styles()


class EstudiosForm(BaseForm):
    class Meta:
        model = Estudios
        fields = [
            "institucion",
            "titulo",
            "description",
            "inicio",
            "fin",
            "mostrar",
            "certificado",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_common_styles()
