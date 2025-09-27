from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from reports.models import BribeReport

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.bribe = BribeReport.objects.create(
            description="Test bribe",
            institution="Test Institution",
            ministry="Test Ministry",
            reported_at="2025-09-27"
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports/home.html')
        self.assertIn('total_reports', response.context)
        self.assertIn('institutions_count', response.context)

    def test_report_bribe_get(self):
        response = self.client.get(reverse('report_bribe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports/report_bribe.html')

    def test_report_bribe_post(self):
        data = {
            'description': 'Another bribe',
            'institution': 'Another Institution',
            'ministry': 'education',
            'reported_at': '2025-09-27',
            'reason': 'To expedite service',
            'amount': '100',
        }
        response = self.client.post(reverse('report_bribe'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success

    def test_report_bribe_post_invalid(self):
        data = {
            'description': 'Test bribe with invalid ministy',
            'institution': 'Another Institution',
            'ministry': 'Invalid Ministry',
            'reported_at': '2025-09-27',
        }
        response = self.client.post(reverse('report_bribe'), data)
        self.assertEqual(response.status_code, 200)  # Form re-rendered

    def test_bribes_list_view(self):
        response = self.client.get(reverse('bribes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports/bribes_list.html')
        self.assertIn('bribes', response.context)

    def test_bribes_list_search(self):
        response = self.client.get(reverse('bribes_list'), {'q': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test bribe')

    def test_contact_view_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports/contact.html')

    def test_contact_view_post(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Hello',
            'message': 'Test message'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302)  # Redirect to success
        self.assertEqual(len(mail.outbox), 2)  # Confirmation + admin email

    def test_contact_success_view(self):
        response = self.client.get(reverse('contact_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports/contact_success.html')

    def test_info_view(self):
        response = self.client.get(reverse('info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports/info.html')