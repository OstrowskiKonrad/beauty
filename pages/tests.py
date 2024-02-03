from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_ulr_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Beauty created by Justyna" " Mastaj</h1>")


class AboutpageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>O mnie</h1>")


class PortfoliopageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/portfolio/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("portfolio"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("portfolio"))
        self.assertTemplateUsed(response, "portfolio.html")

    def test_template_content(self):
        response = self.client.get(reverse("portfolio"))
        self.assertContains(response, "<h1>Moje prace</h1>")


class ClientspageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/klientki/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("clients"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("clients"))
        self.assertTemplateUsed(response, "clients.html")

    def test_template_content(self):
        response = self.client.get(reverse("clients"))
        self.assertContains(response, "<h1>Informacje dla klientek</h1>")


class OfferpageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/oferta/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("offer"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("offer"))
        self.assertTemplateUsed(response, "offer.html")

    def test_template_content(self):
        response = self.client.get(reverse("offer"))
        self.assertContains(response, "<h1>Oferta:</h1>")
