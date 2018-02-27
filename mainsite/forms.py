# coding=UTF-8
from django import forms
from validate_email import validate_email

class orderForm(forms.Form):
    name = forms.CharField(max_length=20, label='imię', widget=forms.TextInput(attrs={'placeholder': u'podaj imię'}))
    surname = forms.CharField(max_length=30, label='naziwsko', widget=forms.TextInput(attrs={'placeholder': u'podaj nazwisko'}))
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'placeholder': u'podaj adres email'}))
    emailConf = forms.EmailField(label='potwierdź email', widget=forms.TextInput(attrs={'placeholder': u'potwierdź adres email'}))
    phone = forms.CharField(max_length=9, required=False, label='telefon', widget=forms.TextInput(attrs={'placeholder': u'podaj numer telefonu'}))

    def clean_emailConf(self):
        mail = self.cleaned_data['email']
        confirmation = self.cleaned_data['emailConf']
        is_valid = validate_email(mail ,verify=True)
        if mail == confirmation and is_valid:
            return confirmation
        else:
            raise forms.ValidationError(u"Potwierdzenie adresu email nie powiodło się. Upewnij się, że został wpisany prawidłowy adres email.")

class contactForm(forms.Form):
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': u'podaj swój adres email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-field'}))

    def clean_email(self):
        mail = self.cleaned_data['email']
        is_valid = validate_email(mail, verify=True)
        if is_valid:
            return mail
        else:
            raise forms.ValidationError(u"Wprowadzony został nieistniejący adres email. Wprowadź poprawny adres.")

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError(u"Wiadomość jest zbyt krótka!")
        return message