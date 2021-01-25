from django.shortcuts import render
#from .models import Details
#from Data_Page.tables import ProjectTable
#from django_tables2 import SingleTableView
#from django.http import HttpResponse
# Create your views here.

def Data_Page(request):
    context = {'name': 'Data_Page Source'}
    return render(request, 'Data_Page.html')

def summary(request):
    return render(request, 'Data_Page/summary.html')

def details(request):

    return render(request, 'details.html')

'''

def details(request):
    content = Details.objects.all()
    context = {
        "content": content
    } 
    return render(request, 'details.html', context)

def item_detail(request, pk):
    project = Project.objects.get(pk=pk)
    item = Details.objects.all()
    context = {
        "item": item
        #'personal_portfolio':project
    }
    return render(request, 'item_detail.html',context)

class ProjectListView(SingleTableView):
   model = Details
   table_class = ProjectTable
'''
   #template_name = 'django_tables2/bootstrap.html'

