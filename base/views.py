from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task

# Create your views here.

@api_view(['GET'])
def apiList(request):
    api_urls = {
        'List': '/task-list/',
    }
    return Response(api_urls)


class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class CustomLogoutView(LogoutView):
    next_page = "login"


class RegisterView(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated = True
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    # if the user is authenticated, he is not allowed to go the register page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("tasks")
        return super(RegisterView, self).get(*args, **kwargs)


# LoginRequiredMixin is to require the user login before they can visit the responsible pages
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    # in class-based-view, the default data object name is object_list, we can change it by editing context_object_name
    context_object_name = "tasks"

    # To restrict that user can and only can get their own data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(complete=False).count()

        # the name in get() should be the same as that in the frontend page.
        # "" means the default value
        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            # we can change the search strategy by changing the attr in filter()
            context["tasks"] = context["tasks"].filter(title__icontains=search_input)
        context["search_input"] = search_input
        return context

    # def get(self):
    #     tasks = self.get_context_data()
    #     return Response(tasks)        


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "detail"
    # change the templete name
    # template_name = ''


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # fields = "__all__"
    # hide users attribute
    fields = ["title", "description", "complete"]
    # after you create the task successfully, return to the main page (point out)
    # reverse_lazy:
    success_url = reverse_lazy("tasks")
    context_object_name = "task_create"
    template_name = "base/task_form.html"

    # let user only create their own tasks.
    def form_valid(self, form) -> HttpResponse:
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task

    fields = ["title", "description", "complete"]
    # exclude = ['user']

    success_url = reverse_lazy("tasks")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")
