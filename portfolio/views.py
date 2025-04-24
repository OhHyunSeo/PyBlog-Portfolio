from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Project, Tag
from .forms import ProjectForm

def project_list(request):
    projects = Project.objects.filter(is_published=True)
    tags = Tag.objects.all()
    
    selected_tag = request.GET.get('tag')
    if selected_tag:
        projects = projects.filter(tags__name=selected_tag)
    
    return render(request, 'portfolio/project_list.html', {
        'projects': projects,
        'tags': tags,
        'selected_tag': selected_tag
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'
    ordering = ['-created_at']

    def get_queryset(self):
        return Project.objects.filter(is_published=True)

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class ProjectCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio/project_form.html'
    success_url = reverse_lazy('portfolio:project_list')

    def form_valid(self, form):
        messages.success(self.request, '프로젝트가 성공적으로 생성되었습니다.')
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio/project_form.html'
    success_url = reverse_lazy('portfolio:project_list')

    def form_valid(self, form):
        messages.success(self.request, '프로젝트가 성공적으로 수정되었습니다.')
        return super().form_valid(form)

class ProjectDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Project
    template_name = 'portfolio/project_confirm_delete.html'
    success_url = reverse_lazy('portfolio:project_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '프로젝트가 성공적으로 삭제되었습니다.')
        return super().delete(request, *args, **kwargs) 