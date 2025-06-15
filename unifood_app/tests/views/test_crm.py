from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from unifood_app.models import Usuario

User = get_user_model()


class CRMDashboardViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='crmuser', password='testpass')
        Usuario.objects.create(user=self.user, ra='9999999999')
        self.client.login(username='crmuser', password='testpass')

    def test_dashboard_page(self):
        response = self.client.get(reverse('crm_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unifood_app/crm/dashboard.html')

