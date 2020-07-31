from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
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
       model = Resume
       fields =[
           'description'
       ]