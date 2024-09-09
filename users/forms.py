from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from users.models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }


class UserEditForm(forms.ModelForm):
    current_password = forms.CharField(label='Contraseña actual', widget=forms.PasswordInput, required=False)
    new_password = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput, required=False)

    email = forms.EmailField(label="Ingrese su email:")
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    website = forms.URLField(label="Enlace a tu página web", required=False)
    description = forms.CharField(widget=forms.Textarea, label="Descripción", required=False)
    profile_image = forms.ImageField(label="Imagen de perfil", required=False)

    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'website', 'description', 'profile_image']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].initial = self.instance.user.email
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name

    def clean(self):
        cleaned_data = super(UserEditForm, self).clean()
        current_password = cleaned_data.get('current_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if current_password and not self.instance.user.check_password(current_password):
            self.add_error('current_password', 'La contraseña actual es incorrecta.')

        if new_password and new_password != confirm_password:
            self.add_error('confirm_password', 'Las contraseñas no coinciden.')

        return cleaned_data

    def save(self, commit=True):
        profile = super(UserEditForm, self).save(commit=False)
        user = profile.user

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if self.cleaned_data['new_password']:
            user.set_password(self.cleaned_data['new_password'])
        profile.website = self.cleaned_data['website']
        profile.description = self.cleaned_data['description']
        if 'profile_image' in self.cleaned_data and self.cleaned_data['profile_image']:
            profile.profile_image = self.cleaned_data['profile_image']

        if commit:
            user.save()
            profile.save()
        return profile