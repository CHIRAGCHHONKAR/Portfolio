from django import forms


#contact form
class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'name',
            'placeholder': 'Full Name'
        })
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address'
        })
    )
    message = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Your Message'
        })
    )