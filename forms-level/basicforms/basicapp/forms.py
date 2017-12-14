from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise ValidationError(_("NAME NEEDS TO START WITH Z"))

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    verify_email = forms.EmailField(label="Enter your email again:")
    '''
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                max_length  = 0)
    '''

    def clean(self):
        all_clean_data = super().clean()  # all at once
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails Match!")
    '''
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidatorError("GOTCHA BOT!")
        return botcatcher
    '''
