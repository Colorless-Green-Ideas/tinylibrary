from django.forms.widgets import TextInput
from django.utils.html import format_html


class PaperTextInput(TextInput):
    def render(self, name, value, attrs=None):
    # Unlike inputs using paper-input-decorator directly, 
    # paper-input does not work out of the box with the native form element.
        html = """<paper-input-decorator label='{0}' floatingLabel>
        <input is="core-input">
        </paper-input-decorator>"""
        return format_html(html, name)