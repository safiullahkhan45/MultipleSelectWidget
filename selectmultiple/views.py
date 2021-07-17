from django.shortcuts import render
from . models import Meal, MealLink
from . forms import MealLinkForm

# Create your views here.
def meals_view(request):

	meals = Meal.objects.all()

	form = MealLinkForm()

	if request.method == 'POST':
		form = MealLinkForm(request.POST)
		if form.is_valid():
			meals_collected = form.cleaned_data.get('meals')
			new_link = MealLink(checkbox_input=form.cleaned_data.get('checkbox_input'))
			new_link.save()
			for meal in meals_collected:
				new_meal = Meal.objects.get(pk=meal.id)
				print(new_meal.name)
				new_link.meals.add(new_meal)

			new_link.save()

		else:
			print(form.errors)

	context = {
		'meals': meals,
		'form': form,
	}

	return render(request, 'selectmultiple/meals.html', context)

