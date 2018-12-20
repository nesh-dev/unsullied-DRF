# Create your tests here.
from django.test import TestCase

from django.urls import reverse

from rest_framework import status

from rest_framework.test import APITestCase

from rest_framework.test import APIClient

from .models import Todo

from .serializers import TodoSerializer


class TodolistTest(APITestCase):
    # client = APIClient()
    url = reverse('todos')
    def setUp(self):
        self.client = APIClient()
        self.data = {'title':'Watch Documentary'}
        # self.response =self.client.post(reverse('todos'),self.data,format="json")
    
    def test_create_task(self):
        """
        Ensure a task can be created
        """
        response =self.client.post(reverse('todos'),self.data,format="json")
        self.assertEqual(201,response.status_code)

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_task(title="", description="", done=False):
        if title != "" and description != "":
            Todo.objects.create(title=title, description=description, done=False)

    def setUp(self):
        self.create_task("skydive", "go to sagana and skydive")
        self.create_task("Hike", "hike in the Himalayas")
        self.create_task("bowling", "go bowling in panari")


# test for a list of all tasks
class GetAllTodo(BaseViewTest):

    def test_get_all_tasks(self):
        response = self.client.get(
            reverse('todos')
        )
        expected = Todo.objects.all()
        serialized = TodoSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingletask(BaseViewTest):

    def get_task(self, pk):
        return self.client.get(reverse("todo", kwargs={
                "pk": pk
            }))

    def test_get_single(self):

        response = self.get_task(1)
        task = Todo.objects.get(pk=1)
        expected = task.title
        self.assertEqual(expected, "skydive")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_single(self):
        self.data = {'title':'Watch Documentary'}
        response = self.client.put(reverse("todo", kwargs={
            "pk":1
        }), self.data,format="json")
    
        self.assertEqual(200, response.status_code)

    def test_delete_single(self):
        response = self.client.delete(reverse("todo", kwargs={
            "pk":1
        }))
        self.assertEqual(204, response.status_code)



