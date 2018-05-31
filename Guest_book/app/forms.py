from django import forms

class CommentForm(forms.Form):
	name = forms.CharField(widget=(forms.TextInput(attrs={'size':10,'placeholder':'Name'})))
	comment = forms.CharField(widget=forms.Textarea())