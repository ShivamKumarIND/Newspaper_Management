from django import forms
from .models import NEWSPAPER_CHOICES


class StartNewspaperForm(forms.Form):
    newspaper = forms.ChoiceField(
        choices=NEWSPAPER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select form-select-lg'})
    )
    location = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your location'})
    )
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your full name'})
    )
    mobile = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter 10-digit mobile number'})
    )

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '').strip()
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Please enter a valid 10-digit mobile number.")
        return mobile


class CloseNewspaperForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your full name'})
    )
    mobile = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter 10-digit mobile number'})
    )
    address = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your address'})
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Please describe the reason for closing...'})
    )

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '').strip()
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Please enter a valid 10-digit mobile number.")
        return mobile


class PaymentCheckForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your full name'})
    )
    mobile = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter 10-digit mobile number'})
    )

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '').strip()
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Please enter a valid 10-digit mobile number.")
        return mobile


class ComplaintForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your full name'})
    )
    mobile = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter 10-digit mobile number'})
    )
    issue = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe your issue in detail...'})
    )

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '').strip()
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Please enter a valid 10-digit mobile number.")
        return mobile


class JoinDistributorForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your full name'})
    )
    mobile = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter 10-digit mobile number'})
    )
    age = forms.IntegerField(
        min_value=18, max_value=70,
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your age (18-70)'})
    )

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '').strip()
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Please enter a valid 10-digit mobile number.")
        return mobile


class NewspaperSoldForm(forms.Form):
    total_received = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Total newspapers received today'})
    )
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your name'})
    )
    mobile = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter 10-digit mobile number'})
    )
    # Newspaper quantities
    hindustan_qty = forms.IntegerField(min_value=0, initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}))
    dainik_jagaran_qty = forms.IntegerField(min_value=0, initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}))
    dainik_bhaskar_qty = forms.IntegerField(min_value=0, initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}))
    prabhat_khabar_qty = forms.IntegerField(min_value=0, initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}))
    aaj_qty = forms.IntegerField(min_value=0, initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}))
    times_of_india_qty = forms.IntegerField(min_value=0, initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}))
    the_hindu_qty = forms.IntegerField(min_value=0, initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}))
    hindustan_times_qty = forms.IntegerField(min_value=0, initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}))
    total_sold = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Total newspapers sold today'})
    )

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '').strip()
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Please enter a valid 10-digit mobile number.")
        return mobile
