from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'İsim ve Soyisminiz',
                'class': 'form-control mb-3'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Mail Adresiniz',
                'class': 'form-control mb-3'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Telefon Numarası',
                'class': 'form-control mb-3 phone-mask',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Mesajın Konusu',
                'class': 'form-control mb-3'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Mesajınız',
                'class': 'form-control mb-3'
            })
        }
        error_messages = {
            'name': {'required': 'Adınızı girin.'},
            'email': {'required': 'E-posta adresinizi girin.', 'invalid': 'Geçerli bir e-posta adresi girin.'},
            'phone': {'required': 'Telefon numaranızı girin.'},
            'subject': {'required': 'Mesajın konusunu girin.'},
            'message': {'required': 'Mesajınızı girin.'},
        }
