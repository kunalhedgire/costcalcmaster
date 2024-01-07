from django.test import TestCase
from django.urls import reverse
from .models import Item
from .views import add_items, save_items, summary, show_add_items


class YourAppViewsTestCase(TestCase):
    def test_add_items_view(self):
        response = self.client.get(reverse('add_items'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_items.html')

    def test_save_items_view(self):
        response = self.client.post(reverse('save_items'), {'price[]': ['10'], 'item[]': ['Item 1']})
        self.assertEqual(response.status_code, 302)  # 302 for redirect

    def test_summary_view(self):
        item = Item.objects.create(price=10, name='Sample Item')
        session_data = self.client.session
        session_data['recent_items'] = [item.id]
        session_data.save()

        response = self.client.get(reverse('summary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'summary.html')

    def test_show_add_items_view(self):
        response = self.client.get(reverse('show_add_items'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_items.html')

    def test_save_items_invalid_data(self):
        response = self.client.post(reverse('save_items'), {'price[]': [''], 'item[]': ['Item 1']})
        self.assertEqual(response.status_code, 302)  # Check for redirect, as empty price is invalid
        self.assertEqual(Item.objects.count(), 0)

    def test_summary_no_recent_items(self):
        response = self.client.get(reverse('summary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'summary.html')
