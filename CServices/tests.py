from django.test import TestCase, RequestFactory
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from blog.views import post_list
from CServices.views import cs_home, cs_wiplog
from django.template.loader import render_to_string
from CServices.models import WipReq
from django.contrib.auth.models import User




class HomePageTest(TestCase):

    def test_root_url_resolves_to_cshome_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_cshome_page_returns_correct_html(self):
        request = HttpRequest()
        response = cs_home(request)
        expected_html = render_to_string('CServices/cs_home.html')
        self.assertEqual(response.content.decode(), expected_html)

class WipRequestModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_admin', email='test@example.com', password='pass')

    def test_saving_and_retrieving_items(self):
        
        first_wip           = WipReq()
        first_wip.author    = self.user
        first_wip.name      = 'Test1'
        first_wip.bid       = 1.5
        first_wip.length    = 10
        first_wip.size      = 1000
        first_wip.cost      = 5000
        first_wip.meth      = 'ONLINE'
        first_wip.save()

        second_wip           = WipReq()
        second_wip.author    = self.user
        second_wip.name      = 'Test2'
        second_wip.bid       = 1.5
        second_wip.length    = 10
        second_wip.size      = 1000
        second_wip.cost      = 5000
        second_wip.meth      = 'ONLINE'
        second_wip.save()

        wips = WipReq.objects.all()
        
        self.assertEqual(wips.count(), 2)
        self.assertEqual(wips[0].name, first_wip.name)
        self.assertEqual(wips[0].meth, first_wip.meth)
        self.assertEqual(wips[1].name, second_wip.name)
        self.assertEqual(wips[1].meth, second_wip.meth)
        

class WipLogDisplayTest(TestCase):

    def test_uses_correct_template(self):
        found = resolve('/wiplog')
        expected_html = ('cs_wiplog.html')
        self.assertEqual(found.func, cs_wiplog)
        self.assertEqual(expected_html, 'cs_wiplog.html')

        
