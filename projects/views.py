

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Project 




class ProjectListView (ListView):
    model: Project
    context_object_name = 'project_list' 
    template_name: 'projects/project_list.html'

    def get_queryset(self):
          return Project.objects.order_by('pk')


    


class ProjectDetailView (DetailView):

    model: Project
    context_object_name = 'project' 
   
    template_name: 'projects/project_detail.html'

    def get_queryset(self):
          return Project.objects.order_by('pk')
