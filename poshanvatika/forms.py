from django import forms 
from .models import DocumentModel


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentModel
        fields = ('title', 'Document',)