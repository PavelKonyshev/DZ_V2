from django.contrib.auth.forms import UserCreationForm
sudo passwd root.from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "password1", "password2")



