# coding=UTF-8
from django import forms

class orderForm(forms.Form):
	name = forms.CharField(max_length=20, label='imię', widget=forms.TextInput(attrs={'placeholder': 'podaj imię'}))
	surname = forms.CharField(max_length=30, label='naziwsko', widget=forms.TextInput(attrs={'placeholder': 'podaj nazwisko'}))
	email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'placeholder': 'podaj adres email'}))
	emailConf = forms.EmailField(label='potwierdź email', widget=forms.TextInput(attrs={'placeholder': 'potwierdź adres email'}))
	phone = forms.CharField(max_length=9, required=False, label='telefon', widget=forms.TextInput(attrs={'placeholder': 'podaj numer telefonu'}))

	def clean_emailConf(self):
		mail = self.cleaned_data['email']
		confirmation = self.cleaned_data['emailConf']
		if mail == confirmation:
			return confirmation
		else:
			raise forms.ValidationError("Potwierdzenie adresu email nie powiodło się")

class contactForm(forms.Form):
	email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'podaj swój adres email'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-field'}))

	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Wiadomość jest zbyt krótka!")
		return message