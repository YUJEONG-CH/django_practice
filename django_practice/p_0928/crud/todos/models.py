from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Todo(models.Model):
    # django에서 pk는 자동으로 만들어짐(id정의 필요x)
    content = models.CharField(max_length = 80)
    completed = models.BooleanField(default=False)


