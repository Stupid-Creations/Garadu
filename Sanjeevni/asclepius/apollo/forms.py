# forms.py
from django import forms
from .models import Report
from accounts.models import Profile


class ReportForm(forms.ModelForm):
    symptom_text = forms.CharField(
        label="Symptoms (comma-separated)",
        help_text="Example: Fever, Cough, Fatigue"
    )
    latitude = forms.FloatField(required=False)
    longitude = forms.FloatField(required=False)

    class Meta:
        model = Report
        fields = ['symptom_text']


    def save(self, user, commit=True):
        print("hello world")

        # Fetch the actual User instance if a dict is passed
        if isinstance(user, dict):
            user = user.get('user', None)

        report = super().save(commit=False)
        print(user)

        try:
            profile = Profile.objects.get(user=user)
            print('profile found')
            print(profile.latitude)
            report.user = user
            report.latitude = profile.latitude
            report.longitude = profile.longitude
        except Profile.DoesNotExist:
            print('profile missing for this user')

        # Save symptoms
        report.symptoms = [s.strip() for s in self.cleaned_data['symptom_text'].split(',')]

        if commit:
            report.save()
        return report

