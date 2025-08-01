from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML, Field, Div, ButtonHolder
from crispy_forms.bootstrap import StrictButton
from deliberasaun_cafi.models import *

class CustomFileInput(forms.ClearableFileInput):
    template_name = 'forms/widgets/custom_file_input.html'

class DeliberasaunForm(forms.ModelForm):
    data_cafi = forms.DateField(
        label='Data CAFI *',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'Hili data CAFI'
        }),
        help_text='Hili data husi deliberasaun CAFI'
    )
    
    no_cafi = forms.CharField(
        label='No. CAFI *',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: CAFI-2024-001'
        }),
        help_text='Numeru identifikasaun deliberasaun CAFI'
    )
    
    linha_ministerio = forms.CharField(
        label='Linha Ministerio *',
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: Ministerio Obras Publicas'
        }),
        help_text='Naran ministerio ka instituisaun'
    )
    
    asunto = forms.CharField(
        label='Asunto *',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Deskreve asunto deliberasaun nian...'
        }),
        help_text='Deskreve asunto deliberasaun ho detallu'
    )
    
    observasaun = forms.CharField(
        label='Observasaun',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Hatama observasaun se iha (opcional)...'
        }),
        help_text='Observasaun adisional (opcional)'
    )
    
    file_attachment = forms.FileField(
        label='File',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '.pdf,.doc,.docx'
        }),
        help_text='Upload dokumentu suporte (PDF, DOC, DOCX - Max: 100MB)'
    )
    anexo = forms.FileField(
        label='Anexo',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '.pdf,.doc,.docx'
        }),
        help_text='Upload dokumentu suporte (PDF, DOC, DOCX - Max: 100MB)'
    )

    class Meta:
        model = Deliberasaun
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
        self.helper.form_class = 'needs-validation'
        self.helper.attrs = {'novalidate': ''}
        
        self.helper.layout = Layout(
            # Form Header
            HTML("""
                <div class="row mb-4">
                    <div class="col-12">
                        <div class="alert alert-light border-start border-primary border-4 mb-0">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-edit text-primary me-3 fa-lg"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold">Formulario Deliberasaun CAFI</h6>
                                    <small class="text-muted">Prenche hotu kampu ne'ebé obrigatoriu (*) ho informasaun loos</small>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            """),
            
            # First Row: CAFI Number, Ministry, Date - Side by side
            HTML("""
                <div class="row mb-3">
                    <div class="col-md-4">
                        <div class="mb-3">
            """),
            Field('no_cafi', css_class='form-control'),
            HTML("""
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="mb-3">
            """),
            Field('linha_ministerio', css_class='form-control'),
            HTML("""
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="mb-3">
            """),
            Field('data_cafi', css_class='form-control'),
            HTML("""
                        </div>
                    </div>
                </div>
            """),
            
            # Second Row: Subject and File - Side by side
            HTML("""
                <div class="row mb-3">
                    <div class="col-md-4">
                        <div class="mb-3">
            """),
            Field('asunto', css_class='form-control'),
            HTML("""
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="mb-3">
            """),
            Field('file_attachment', css_class='form-control'),
            HTML("""
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="mb-3">
            """),
            Field('anexo', css_class='form-control'),
            HTML("""
                        </div>
                    </div>
                </div>
            """),
            
            # Third Row: Observations (full width)
            HTML("""
                <div class="row mb-4">
                    <div class="col-md-12">
                        <div class="mb-3">
            """),
            Field('observasaun', css_class='form-control'),
            HTML("""
                        </div>
                    </div>
                </div>
            """),
            
            # Form Actions
            HTML("""
                <div class="row">
                    <div class="col-12">
                        <div class="d-flex justify-content-between align-items-center p-3 bg-light rounded border">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-info-circle text-info me-2"></i>
                                <small class="text-muted">Verifika hotu informasaun molok ita submete</small>
                            </div>
                            <div class="d-flex gap-2">
                                <a href="{% url 'deliberasaun' %}" class="btn btn-outline-secondary">
                                    <i class="fas fa-times me-1"></i>Kansela
                                </a>
                                <button type="submit" class="btn btn-primary">
                                    <i class="fas fa-save me-1"></i>Rai Deliberasaun
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            """),
        )

        # Enhanced field styling and validation
        for field_name, field in self.fields.items():
            # Add required indicator to labels
            if field.required:
                field.widget.attrs['required'] = 'required'
            
            # Add Bootstrap validation classes
            field.widget.attrs.update({
                'class': field.widget.attrs.get('class', '') + ' form-control'
            })
            
            # Custom file input widget
            if field.widget.__class__.__name__ == 'ClearableFileInput':
                field.widget = CustomFileInput()
                field.widget.attrs.update({
                    'class': 'form-control',
                    'accept': '.pdf,.doc,.docx'
                })

    def clean_file_attachment(self):
        """Validate file upload"""
        file = self.cleaned_data.get('file_attachment')
        if file:
            # Check file size (10MB limit)
            if file.size > 100 * 1024 * 1024:
                raise forms.ValidationError('Dokumentu boot liu (max: 100MB)')
            
            # Check file extension
            allowed_extensions = ['.pdf', '.doc', '.docx']
            file_extension = file.name.lower().split('.')[-1]
            if f'.{file_extension}' not in allowed_extensions:
                raise forms.ValidationError('Formatu dokumentu la suporta. Uza: PDF, DOC, DOCX')
        
        return file

    def clean_no_cafi(self):
        """Validate CAFI number format"""
        no_cafi = self.cleaned_data.get('no_cafi')
        if no_cafi:
            # Basic format validation
            if len(no_cafi) < 5:
                raise forms.ValidationError('No. CAFI tenki iha karakter 5 ka liu')
        return no_cafi