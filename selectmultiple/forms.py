from django import forms
from . models import Meal, MealLink


class MealLinkForm(forms.Form):

	meals = forms.ModelMultipleChoiceField(
		queryset = Meal.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
	checkbox_input = forms.CharField(max_length=30)


# class MealLinkForm(forms.ModelForm):


# 	class Meta:
# 		model = MealLink
# 		fields = ['meals', 'checkbox_input']

# 	def __init__(self, *args, **kwargs):
# 		super(MealLinkForm, self).__init__(*args, **kwargs)
# 		self.fields['meal'] =  forms.ModelMultipleChoiceField(
# 			queryset = Meal.objects.all(),
# 			widget  = forms.CheckboxSelectMultiple,
# 		)