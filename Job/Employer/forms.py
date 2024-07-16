# from .models import PostJob, Skill
# from django import forms


# class PostJobForm(forms.ModelForm):
#     job_title = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class":"form-control"
#             }
#         )
#     )
#     skills = forms.ModelMultipleChoiceField(
#         queryset=Skill.objects.all(),  # Queryset for available skills
#         widget=forms.CheckboxSelectMultiple,  # Use checkboxes for selection
#         required = True
#     )

#     class Meta:
#         model = PostJob
#         fields = ['job_title', 'location' ,'job_desc', 'company_name', 'salary' ,'Employment_Type', 'deadline', 'company_info' ,'skills']

# class PostJobForm(forms.ModelForm):
#     skills = forms.ModelMultipleChoiceField(
#         queryset=Skill.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True
#     )

#     class Meta:
#         model = PostJob
#         fields = ['job_title', 'company_name', 'skills']  # i

# from django import forms
# from .models import PostJob, Skill

# class PostJobForm(forms.ModelForm):
#     skills = forms.ModelMultipleChoiceField(
#         queryset=Skill.objects.all(),
#         widget=forms.SelectMultiple(attrs={'class': 'form-select', 'multiple': 'multiple'}),
#         required=True
#     )

#     class Meta:
#         model = PostJob
#         fields = ['job_title', 'company_name', 'skills']  # include other fields as needed

from django import forms
from .models import PostJob,Skill

class PostJobForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select', 'multiple': 'multiple'}),
        required=True
    )

    class Meta:
        model = PostJob
        fields = ['job_title', 'job_desc', 'location', 'Employment_Type', 'salary', 'skills', 'company_name', 'company_info', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
