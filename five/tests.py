from django.test import TestCase
from django.urls import reverse
from .models import Todo as Task

class TaskFlowTests(TestCase):
    def test_create_task_minimal(self):
        self.assertEqual(Task.objects.count(), 0)
        resp = self.client.post(reverse('five:task_create'), {
            'title': 'Buy milk',
            'description': '2% gallon',
        })
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)

    def test_task_list_shows_created_tasks(self):
        # Pre-create two todos
        from .models import Todo as Task
        Task.objects.create(title='A')
        Task.objects.create(title='B')

        resp = self.client.get(reverse('five:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'A')
        self.assertContains(resp, 'B')

    def test_edit_task(self):
        from .models import Todo as Task
        t = Task.objects.create(title='Old')
        resp = self.client.post(reverse('five:task_edit', args=[t.pk]), {
            'title': 'New',
        })
        self.assertEqual(resp.status_code, 302)  # expect redirect after edit
        t.refresh_from_db()
        self.assertEqual(t.title, 'New')

    def test_delete_task(self):
        from .models import Todo as Task
        t = Task.objects.create(title='Gone soon')
        self.assertEqual(Task.objects.count(), 1)
        resp = self.client.post(reverse('five:task_delete', args=[t.pk]))
        self.assertEqual(resp.status_code, 302)  # expect redirect after delete
        self.assertEqual(Task.objects.count(), 0)

    def test_toggle_complete(self):
        from .models import Todo as Task
        t = Task.objects.create(title='Toggle me', completed=False)
        # first toggle -> should become True
        resp1 = self.client.get(reverse('five:task_toggle', args=[t.pk]))
        self.assertEqual(resp1.status_code, 302)
        t.refresh_from_db()
        self.assertTrue(t.completed)
        # second toggle -> should become False
        resp2 = self.client.get(reverse('five:task_toggle', args=[t.pk]))
        self.assertEqual(resp2.status_code, 302)
        t.refresh_from_db()
        self.assertFalse(t.completed)
    
    def test_move_up_and_down(self):
        from .models import Todo as Task
        a = Task.objects.create(title='A')
        b = Task.objects.create(title='B')

        # Try to move B up (should swap order later once implemented)
        resp1 = self.client.get(reverse('five:task_move', args=[b.pk, 'up']))
        self.assertEqual(resp1.status_code, 302)

        # After we implement positions, we'll assert on positions here.
        # For now, this test just drives the route into existence.

        # Try to move B down (route should exist)
        resp2 = self.client.get(reverse('five:task_move', args=[b.pk, 'down']))
        self.assertEqual(resp2.status_code, 302)


# Create your tests here.
