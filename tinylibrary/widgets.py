from django.forms.widgets import TextInput
from django.utils.html import format_html


class PaperTextInput(TextInput):
    def render(self, name, value, attrs=None):
        return format_html("<paper-input label='{0}' floatingLabel></paper-input>", name)