from django.shortcuts import render

from journal.models import Group


# Create your views here.
def index_view(request):
    return render(request, 'journal/index.html')

def contact_view(request):
    return render(request, 'journal/contacts.html')


def about_view(request):
    return render(request, 'journal/about.html')

def student_view(request):
    student_list = [
        {'name': 'Евсеев', 'status': 'Двоечник'},
        {'name': 'Золотухин', 'status': 'Троечник'},
        {'name': 'Коновалов', 'status': 'Отличник'},
    ]

    context = {
        'page_title': 'Список учеников',
        'student_list': student_list,
    }

    return render(request, 'journal/student.html', context)

def groups_view(request):
    all_groups = Group.objects.all()

    context = {
        'page_title': 'Список учебных групп',
        'groups_list': all_groups,
    }

    return render(request, 'journal/groups.html', context)





