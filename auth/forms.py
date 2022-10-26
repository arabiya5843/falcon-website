# from django.contrib.auth.models import User
# from django import forms
#
#
# class LoginForm(forms.ModelForm):
#     confirm_password = forms.PasswordInput()
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'email', 'password']
#         widgets = {
#             'first_name': forms.CharField(widget={
#                 'class': 'form-control',
#                 'autocomplete': 'on',
#                 'placeholder': 'Name',
#             }),
#             'email': forms.CharField(widget={
#                 'class': 'form-control',
#                 'autocomplete': 'on',
#                 'placeholder': 'Email',
#             }),
#             'password': forms.CharField(widget={
#                 'class': 'form-control',
#                 'autocomplete': 'on',
#                 'placeholder': 'Password',
#             }),
#             'confirm_password': forms.CharField(widget={
#                 'class': 'form-control',
#                 'autocomplete': 'on',
#                 'placeholder': 'Confirm Password',
#             }),
#         }
