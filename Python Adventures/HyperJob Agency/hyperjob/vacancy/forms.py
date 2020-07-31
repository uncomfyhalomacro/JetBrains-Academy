from django import forms
from .models import Vacancy

class VacancyForm(forms.ModelForm):
   description = forms.CharField(
       required=False,
       widget=forms.Textarea(
           attrs={
               "placeholder": "Your description",
               "id": "res_desc" ,
               "rows": 20,
               "cols": 120
           }
       )
   )
   class Meta:
       model = Vacancy
       fields =[
           'description'
       ]