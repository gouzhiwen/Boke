from django import forms
from BoKe.models import Comments

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comments
        fileds = ['name','content']