from django.db import models
from django.contrib.auth.models import User

# @Author Daniel C (all commented for now)

# We want a @oneToMany rel. for User and todoItem -> use foreing key

# class PercentageField(fields.FloatField):
#     widget = fields.TextInput(attrs={"class": "percentInput"})

#     def to_python(self, value):
#         val = super(PercentageField, self).to_python(value)
#         if is_number(val):
#             return val/100
#         return val

#     def prepare_value(self, value):
#         val = super(PercentageField, self).prepare_value(value)
#         if is_number(val) and not isinstance(val, str):
#             return str((float(val)*100))
#         return val


# # model for todos
# class todoItem(model.Model):
#     description = models.TextField(max_length=160)
#     deadline = models.DateTimeField()
#     percent = models.IntegerField()

#     # @param User: Related Table
#     # @pam on_delete: if User gets delete, then delete todoItem (-->)
#     author = model.ForeingKey(User, on_delete=models.CASCADE)