from django import forms


ALGORITHM_CHOICES = [
  ('bubbleSort','bubblesort'),
  ('insertionSort','insertionsort'),
]

class SortingForm(forms.Form):
  numbers = forms.CharField(label='numbers', max_length=100)
  algorithm = forms.CharField(label='select your algortihm', widget=forms.Select(choices=ALGORITHM_CHOICES))