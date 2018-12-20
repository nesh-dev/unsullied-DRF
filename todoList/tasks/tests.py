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

<<<<<<< HEAD

=======
    # def test_can_get_all_tasks(self):
    #     """Test if api can get the task list"""
    #     todos = Todo.objects.all()
    #     response  = self.client.get(self.url)
    #     self.assertEqual(200,response.status_code)

    #     serialized_data =TodoSerializer(todos,)
>>>>>>> 8052e6173689a745cde6d3bf0ddc7d35b9424c55

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
<<<<<<< HEAD
        return self.client.get(reverse("todo", kwargs={
                "pk": pk
            })
            
=======
        self.client.get(
            "todo", kwargs={
                "pk": pk
            }
>>>>>>> 8052e6173689a745cde6d3bf0ddc7d35b9424c55
        )

    def test_get_single(self):

        response = self.get_task(1)
        task = Todo.objects.get(pk=1)
        expected = task.title
        self.assertEqual(expected, "skydive")
<<<<<<< HEAD
        self.assertEqual(response.status_code, status.HTTP_200_OK)
=======
        self.assertEqual(200,response.status_code)
>>>>>>> 8052e6173689a745cde6d3bf0ddc7d35b9424c55




