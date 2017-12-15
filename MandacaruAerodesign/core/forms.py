from django import forms

class FormContato(forms.Form):
    nomeContato = forms.CharField(required=True, max_length = 100)
    emailContato = forms.CharField(required=True)
    telefoneContato = forms.CharField(required=True)
    mensagemContato = forms.CharField(required=True, widget=forms.Textarea)
