from django.db import models


class Todo(models.Model):
    """
    Todo Model
    Defines attributes of a todo/task
    """
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.title

    objects = models.Manager()
