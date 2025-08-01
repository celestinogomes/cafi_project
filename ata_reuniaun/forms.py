from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML, Field, Div, ButtonHolder
from crispy_forms.bootstrap import StrictButton
from ata_reuniaun.models import *

class CustomFileInput(forms.ClearableFileInput):
    template_name = 'forms/widgets/custom_file_input.html'

class AtaForm(forms.ModelForm):
    data_ata = forms.DateField(
        label='Data Ata *',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'Hili data Ata'
        }),
        help_text='Hili data Ata'
    )
    
    no_ata = forms.CharField(
        label='No. Ata *',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 25/XII/CAFI/2024'
        }),
        help_text='Numeru identifikasaun ATA reuniaun'
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
            'placeholder': 'Deskreve asunto Ata Reuniaun nian...'
        }),
        help_text='Deskreve asunto ATA ho detallu'
    )
    
    diversos = forms.CharField(
        label='Diversos',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Hatama observasaun se iha (opcional)...'
        }),
        help_text='Diversos adisional (opcional)'
    )
    
    file_attachment = forms.FileField(
        label='Dokumentu Suporte',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '.pdf,.doc,.docx'
        }),
        help_text='Upload dokumentu suporte (PDF, DOC, DOCX - Max: 10MB)'
    )

    class Meta:
        model = Ata
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
                                    <h6 class="mb-1 fw-bold">Formulario ATA Reuniaun</h6>
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
            Field('no_ata', css_class='form-control'),
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
            Field('data_ata', css_class='form-control'),
            HTML("""
                        </div>
                    </div>
                </div>
            """),
            
            # Second Row: Subject and File - Side by side
            HTML("""
                <div class="row mb-3">
                    <div class="col-md-8">
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
                </div>
            """),
            
            # Third Row: Observations (full width)
            HTML("""
                <div class="row mb-4">
                    <div class="col-md-12">
                        <div class="mb-3">
            """),
            Field('diversos', css_class='form-control'),
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
                                    <i class="fas fa-save me-1"></i>Rai Ata Reuniaun
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
            if file.size > 50 * 1024 * 1024:
                raise forms.ValidationError('Dokumentu boot liu (max: 10MB)')
            
            # Check file extension
            allowed_extensions = ['.pdf', '.doc', '.docx']
            file_extension = file.name.lower().split('.')[-1]
            if f'.{file_extension}' not in allowed_extensions:
                raise forms.ValidationError('Formatu dokumentu la suporta. Uza: PDF, DOC, DOCX')
        
        return file

    def clean_no_ata(self):
        """Validate CAFI number format"""
        no_ata = self.cleaned_data.get('no_ata')
        if no_ata:
            # Basic format validation
            if len(no_ata) < 5:
                raise forms.ValidationError('No. CAFI tenki iha karakter 5 ka liu')
        return no_ata