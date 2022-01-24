from django.shortcuts import render
from .forms import SortingForm

def bubbleSort(nts):
  nts_len = len(nts)
  for i in range(nts_len):
    for p in range(nts_len -i -1):
      if nts[p] > nts[p+1]:
        nts[p], nts[p+1] = nts[p+1], nts[p]
  return nts

def insertionSort(nts):
  for i in range(1, len(nts)):
    current_num = nts[i]
    p = i - 1
    while p >=0 and nts[p] > current_num:
      nts[p+1] = nts[p]
      p -=1

      nts[p+1] = current_num
  return nts

def home(request):
  form = SortingForm()
  return render(request,"home.html",{'form':form})

def processing(request):
  if request.method == 'POST':
    form = SortingForm(request.POST)
    if form.is_valid:
      x = request.POST['numbers']
      y = request.POST['algorithm']
      list_of_strings= x.split()
      map_object = map(int, list_of_strings)
      list_of_integers = list(map_object)
      print(list_of_integers)
      data=globals()[y](list_of_integers)
      print(data)


  return render(request, "processing.html", {'data':data})  
