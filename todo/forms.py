# Adding a task by form like admin page but in html browser which we made

from pyexpat import model
from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta():
        model = Todo

        #we can change fields to specify to list
        # for ex, fields = ['title', 'desc', 'pub_date']
        fields = ['title', 'desc', 'pub_date', 'completed']

