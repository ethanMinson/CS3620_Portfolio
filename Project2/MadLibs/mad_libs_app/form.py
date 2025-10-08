from django import forms

from mad_libs_app.models import FinishedStory


class MadLibForm(forms.Form):
    def __init__(self, blanks, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i, blank in enumerate(blanks):
            field_name = f"blank_{i}"
            self.fields[field_name] = forms.CharField(
                label=blank.capitalize(),
                required=True,
                widget=forms.TextInput(attrs={'placeholder': 'Enter a '+blank, 'size': '30'})
            )
