from django.test import TestCase
from portafolio.models import SobreMi, SocialLink, Projecto, Experiencia, Estudios


class SobreMiTestCase(TestCase):
    def setUp(self):
        SobreMi.objects.create(
            nombre="Juan",
            apellido="Pérez",
            descripcion="Desarrollador de software",
            perfil="sobremi/perfil.jpg",
            fondo="sobremi/fondo.jpg",
        )

    def test_sobremi_creation(self):
        sobremi = SobreMi.objects.first()
        self.assertEqual(sobremi.full_name(), "Juan Pérez")
        self.assertEqual(sobremi.descripcion, "Desarrollador de software")

    def test_single_instance(self):
        with self.assertRaises(Exception):
            SobreMi.objects.create(
                nombre="Otro",
                apellido="Usuario",
                descripcion="Otro registro",
                perfil="sobremi/perfil2.jpg",
                fondo="sobremi/fondo2.jpg",
            )


class SocialLinkTestCase(TestCase):
    def setUp(self):
        SocialLink.objects.create(
            title="GitHub",
            url="https://github.com/user",
            svg="<svg></svg>",
            activo=True,
        )

    def test_social_link_creation(self):
        social_link = SocialLink.objects.first()
        self.assertEqual(social_link.title, "GitHub")
        self.assertEqual(social_link.url, "https://github.com/user")
        self.assertTrue(social_link.activo)


class ProjectoTestCase(TestCase):
    def setUp(self):
        Projecto.objects.create(
            title="Proyecto 1",
            description="Descripción del proyecto 1",
            repository="https://github.com/user/proyecto1",
            pagina="https://proyecto1.com",
            image="project/proyecto1.jpg",
            inicio="2023-01-01",
            fin="2023-12-31",
        )

    def test_project_creation(self):
        proyecto = Projecto.objects.first()
        self.assertEqual(proyecto.title, "Proyecto 1")
        self.assertEqual(proyecto.repository, "https://github.com/user/proyecto1")
        self.assertEqual(proyecto.pagina, "https://proyecto1.com")


class ExperienciaTestCase(TestCase):
    def setUp(self):
        Experiencia.objects.create(
            empresa="Empresa X",
            cargo="Desarrollador",
            description="Trabajé como desarrollador backend.",
            url="https://empresax.com",
            inicio="2022-01-01",
            fin="2023-01-01",
            mostrar=True,
        )

    def test_experiencia_creation(self):
        experiencia = Experiencia.objects.first()
        self.assertEqual(experiencia.empresa, "Empresa X")
        self.assertEqual(experiencia.cargo, "Desarrollador")
        self.assertTrue(experiencia.mostrar)


class EstudiosTestCase(TestCase):
    def setUp(self):
        Estudios.objects.create(
            institucion="Universidad X",
            titulo="Ingeniería en Sistemas",
            description="Carrera en ingeniería de sistemas.",
            inicio="2018-01-01",
            fin="2022-12-31",
            mostrar=True,
            certificado="certificados/certificado1.pdf",
        )

    def test_estudios_creation(self):
        estudio = Estudios.objects.first()
        self.assertEqual(estudio.institucion, "Universidad X")
        self.assertEqual(estudio.titulo, "Ingeniería en Sistemas")
        self.assertTrue(estudio.mostrar)
