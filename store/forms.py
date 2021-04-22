from django import forms
from .models import Store, Category
from django.core.exceptions import ValidationError

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = "__all__"
        exclude =("Isbn",)

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) <10 or len(title)>50:
            raise ValidationError("title shouldn be between 10 to 50 chars")
        return title


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


    def clean(self):
        super(CatForm, self).clean()
        name = self.cleaned_data.get("name")

        if len(name) < 2:
            raise ValidationError("content must be bigger than 2 chars")

        return self.cleaned_data