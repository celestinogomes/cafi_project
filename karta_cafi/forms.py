from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML, Field, Div
from karta_cafi.models import *

class CustomFileInput(forms.ClearableFileInput):
    template_name = 'forms/widgets/custom_file_input.html'

class KartaTamaForm(forms.ModelForm):
    data_karta = forms.DateField(label='Data Karta', widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    data_tama = forms.DateField(label='Data Karta Tama', widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    class Meta:
        model = ConviteCafi
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    Field('no_referensia', css_class='form-control'),
                    css_class='col-md-4',
                ),
                Div(
                    Field('data_convite', css_class='form-control'),
                    css_class='col-md-4',
                ),
                Div(
                    Field('dirije_ba', css_class='form-control'),
                    css_class='col-md-4',
                ),
                css_class='row',
            ),
            Div(
                Div(
                    Field('linha_ministerio', css_class='form-control'),
                    css_class='col-md-6',
                ),
                Div(
                    Field('file_attachment', css_class='form-control'),
                    css_class='col-md-6',
                ),
                css_class='row',
            ),
            Div(
                Div(
                    Field('asunto', css_class='form-control'),
                    css_class='col-md-12',
                ),
                css_class='row',
            ),
            
            Div(
                HTML("<button class='btn mt-2 btn-primary btn-md col-sm-2 mx-auto' type='submit'>Submit</button>"),
                css_class='row mx-auto',
            ),
        )

        for field in self.fields.values():
            if field.widget.__class__.__name__ == 'ClearableFileInput':
                field.widget = CustomFileInput()
                field.widget.attrs.update({
                    'class': 'form-control',
                })

class KartaSaiForm(forms.ModelForm):
    data_reuniaun = forms.DateField(label='Data Reuniaun', widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    data_sai = forms.DateField(label='Data Karta Sai', widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    class Meta:
        model = AgendaCafi
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    Field('no_karta', css_class='form-control'),
                    css_class='col-md-3',
                ),
                Div(
                    Field('no_referensia', css_class='form-control'),
                    css_class='col-md-3',
                ),
                Div(
                    Field('data_reuniaun', css_class='form-control'),
                    css_class='col-md-3',
                ),
                Div(
                    Field('data_sai', css_class='form-control'),
                    css_class='col-md-3',
                ),
                css_class='row',
            ),
            Div(
                Div(
                    Field('asunto', css_class='form-control'),
                    css_class='col-md-6',
                ),
                Div(
                    Field('dirije_ba', css_class='form-control'),
                    css_class='col-md-6',
                ),
                css_class='row',
            ),
            Div(
                Div(
                    Field('linha_ministerio', css_class='form-control'),
                    css_class='col-md-6',
                ),
                Div(
                    Field('file_attachment', css_class='form-control'),
                    css_class='col-md-6',
                ),
                css_class='row',
            ),
            Div(
                HTML("<button class='btn mt-2 btn-primary btn-md col-sm-2 mx-auto' type='submit'>Submit</button>"),
                css_class='row mx-auto',
            ),
        )

        for field in self.fields.values():
            if field.widget.__class__.__name__ == 'ClearableFileInput':
                field.widget = CustomFileInput()
                field.widget.attrs.update({
                    'class': 'form-control',
                })