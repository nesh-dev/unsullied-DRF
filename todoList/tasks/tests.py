# Create your tests here.
from django.test import TestCase

from django.urls import reverse

from rest_framework import status

from rest_framework.test import APITestCase

from .models import Todo


class TodolistTest(APITestCase):
    # client = APIClient()
    url = reverse('todos')
    def setUp(self):
        self.client = APIClient()
        self.todo-data = {'title':'Watch Documentary'}
        self.response =self.client.post(reverse('tasks'),self.todo-data,format="json")
    
    def test_create_task(self):
        """
        Ensure a task can be created
        """
        # response = client.post(/task/,{'title':'Eat'})
        self.assertEqual(201,response.status_code)

    # def test_can_get_all_tasks(self):
    #     """Test if api can get the task list"""
    #     todos = Todo.objects.all()
    #     response  = self.client.get(self.url,self.todo-data,format="json")

    # def test_can_get_single_task(self):
    #     """Test if api can get the task list"""

