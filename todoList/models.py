from django.db import models

# model for todos
class todoItem(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=160)
    deadline = models.DateTimeField() # ...
    percent = models.IntegerField() # Needs to be between 0 and 100!

    def __str__(self):
        return self.id


# TODO:
# - Still figure out who to edit, save and *delete todoItems from DB
# - Format @param deadline and @param percent in @class todoItem