from django import forms
from django.core.validators import validate_email

class MultiEmailField(forms.Field):
    def to_python(self, value):
        if not value:
            return []
        #Modify the input so that email can be split by , and ;
        #For copying and pasting email address from the list, None, () \ will be removed.
        value = value.replace(' ', '')
        value = value.replace('None,', '')
        value = value.replace(';', ',')
        value = value.replace(',,', ',')
        print(value)
        while value.endswith(',') or value.endswith(';'):
            value = value[:-1] #remove the last ',' or ';'

        return value.split(',')

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super(MultiEmailField, self).validate(value)
        for email in value:
            validate_email(email)

class MailForm(forms.Form):
    email = MultiEmailField(required=False, help_text='Split email by " ,  " or " ; ", or copy paste a list from below')
    email_all_users = forms.BooleanField(required=False)
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

