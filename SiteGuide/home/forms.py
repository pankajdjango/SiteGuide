from django import forms
from .models import Patient
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['first_name','last_name','gender','age','doctor_name','doctor_fees','started_meds_on_date','disease_Problem']
    
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():visible.field.widget.attrs['class'] = 'form-control'

    started_meds_on_date = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))