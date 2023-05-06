from django.test import TestCase

from django.test import TestCase
from django.urls import reverse

class DemoTests(TestCase):
    """ demostrate basic testing in TDD!"""

    def test_ping_get(self):
        """ Get ping """
        response = self.client.get("/ping/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(
            response.content.decode("utf8"), "pong"
        )

    def test_ping_head(self):
        """ Head Ping"""    
        response = self.client.head("/ping/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content,b"")
        self.assertGreater(
            int(response["Content-Length"]),
                0
        )

    def test_ping_options(self):
        """ Options Ping"""
        response = self.client.options("/ping/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(int(response["Content-Length"]),0)
        for method in ["GET","HEAD","OPTIONS"]:
            with self.subTest(method=method):
                self.assertIn(
                    method, response["Allow"],
                    f"{method} not in Allow header",
                )

    def test_ping_method_not_allowed(self):
        """" do we handle disallowed methods? """
        not_allowed = [
            "post", 
            "put", 
            "delete", 
            "patch", 
            "trace"
        ]
        for method in not_allowed:
            with self.subTest(method=method):
                call_method = getattr(self.client,method)
                response = call_method("/ping/")
                self.assertEqual(response.status_code,405)


    # def test_status_get(self):                
    #     """ Test the status page """
    #     url = reverse("site_status")
    #     self.assertEqual(url, "/status/")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code,200)
    #     self.assertTemplateUsed(response,"base.html")
    #     self.assertTemplateUsed(response,"testapp/base.html")
    #     self.assertTemplateUsed(response,"testapp/status.html")
    #     self.assertIn("status",response.context)
    #     # Django provides its own assertions
    #     # 
    #     self.assertInHTML(
    #         "<p>Status is Good</p>",
    #         response.content.decode("utf8"),
    #     )
