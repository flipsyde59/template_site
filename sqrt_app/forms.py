from django.forms import ModelForm, ChoiceField, Form
import django.forms as forms

EPS_CHOICES = ((i, i) for i in range(10))
LANGUAGE_CHOISES = (('eng', 'English'), ('rus', 'Russian'), ('chi', 'Chinese'), ('spa', 'Spanish'))


class LangForm (Form):
    #def __init__(self, *args, **kwargs):
     #   super(LangForm, self).__init__(*args, **kwargs)
      #  self.fields['title'] =
    title = ChoiceField(choices=LANGUAGE_CHOISES)