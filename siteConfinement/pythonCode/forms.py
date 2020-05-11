from django.http import HttpRequest
from django.contrib.auth import authenticate, login, get_user_model
from django import forms


User=get_user_model()


class UserLoginForm(forms.Form):
    mail = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self,*args, **kwargs):
        mail = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        
        if mail and password:
            user = authenticate(mail=mail,password=password)
            if not user:
                raise forms.ValidationError("Cet utilisateur n'existe pas")
            if not user.check_password(password):
                raise forms.ValidationError('Mot de passe incorrect')
            if not user.is_active:
                raise forms.ValidationError("Cet utilisateur n'est plus actif")
        return super(UserLoginForm(),self).clean(*args,**kwargs)
    
class UserRegisterForm (forms.ModelForm):
    name = forms.CharField()
    first_name = forms.CharField()
    email = forms.EmailField()
    adress = forms.CharField()
    tel = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields = [
            'name-input-field',
            'firstname-input-field',
            'email-input-field',
            'adress-input-field',
            'tel-input-field',
            'password-input-field',
            'repeat-password-field'
        ]
        
    def clean_email(self):
        name=self.cleaned_data('name-input-field')
        first_name=self.cleaned_data('firstname-input-field')
        email = self.cleaned_data('email-input-field')
        adress = self.cleaned_data('adress-input-field')
        password = self.cleaned_data('password-input-field')
        password2 = self.cleaned_data('repeat-password-field')
        if password != password2:
            raise forms.ValidationError("Les 2 mot de passe doivent être les mêmes")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Cet adresse mail est déjà utilisée")
        return email
    
    






#def Connexion(request):
#    username = request.POST['email']
#    password = request.POST['password']
#    user = authenticate(request, username=username, password=password)
#    if user is not None:
#        login(request, user)
        # Redirect to a success page.
#        ...
#    else:
        # Return an 'invalid login' error message.
#        ...

