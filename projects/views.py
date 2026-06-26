from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Project


def project_list(request):

    query = request.GET.get('q')

    projects = Project.objects.all()

    if query:

        projects = projects.filter(
            Q(title__icontains=query) |
            Q(location__icontains=query) |
            Q(description__icontains=query)
        )

    paginator = Paginator(projects, 6)

    page_number = request.GET.get('page')

    projects = paginator.get_page(page_number)

    context = {
        'projects': projects
    }

    return render(
        request,
        'projects/project_list.html',
        context
    )

def project_detail(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk
    )

    context = {
        'project': project
    }

    return render(
        request,
        'projects/project_detail.html',
        context
    )
