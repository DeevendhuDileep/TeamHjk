from django.shortcuts import render

# Create your views here.


def load_first_page(request):
    return render(request,'firstpage.html',{'key':'value'})

def load_second_page(request):
    context = {'animal':'dog','flower':'rose','fruit':'apple'}
    return render(request,'secondpage.html',context)



