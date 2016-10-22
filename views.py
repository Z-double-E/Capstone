"""
Definition of views.
"""
from django.http import Http404
from .models import Problem, ProblemSet
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpRequest
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from app import forms
from .forms import UserForm
from django.contrib.auth import authenticate, login

## home page method that will display all problems
def home(request):
    """Renders the home page."""
    form = forms.SearchProblem
    if request.method == "POST":
        searched_problems = []
        problemSP = request.POST.get('problemSP')
        dp = request.POST.get('dp')
        type = request.POST.get('type')
        if problemSP == "" and dp == "" and type == "":
            p = Problem.objects.all()
            # p = Problem.objects.filter(problemSP=problemSP,dp=dp,type=type)
        elif dp == "" and type == "":
            p = Problem.objects.filter(problemSP=problemSP)
        elif problemSP == "" and type == "":
            p = Problem.objects.filter(dp=dp)
        elif problemSP == "" and dp == "":
            p = Problem.objects.filter(type=type)
        elif problemSP == "":
            p = Problem.objects.filter(dp=dp, type=type)
        elif dp == "":
            p = Problem.objects.filter(problemSP=problemSP, type=type)
        elif type == "":
            p = Problem.objects.filter(problemSP=problemSP, dp=dp)
        else:
            p = Problem.objects.filter(problemSP=problemSP, dp=dp, type=type)

        for i in p:
            if i not in searched_problems:
                searched_problems.append(i)

        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'form' : form,
                'all_problems': searched_problems,
                'year': datetime.now().year,
            }
        )

    else:
        all_problems = Problem.objects.all()
        print(all_problems)
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'form' : form,
                'all_problems': all_problems,
                'year': datetime.now().year,
            }
        )


##method to dispaly problem all problem sets
def problems(request):
    Sets = ProblemSet.objects.all()
    print(Sets)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/problems.html',
        {
            'title':'Problem Sets',
            'Sets': Sets,
            'year':datetime.now().year,
        }
    )


##method to dispaly problem a problem set
def problemSet(request, problemset_id):
    try:
        Set = ProblemSet.objects.get(pk=problemset_id)
    except ProblemSet.DoesNotExist:
        raise Http404("problem does not exist")
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/problemSet.html',
        {
            'title': Set.name,
            'Set': Set,
            'year':datetime.now().year,
        }
    )


##method to dispaly problem
def detail(request, problem_id):
    try:
        problem = Problem.objects.get(pk=problem_id)
        problem.Noviews+=1
        problem.save()
    except Problem.DoesNotExist:
        raise Http404("problem does not exist")
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/details.html',
        {
            'title':'Details',
            'problem': problem,
            'year':datetime.now().year,
        }
    )


##method to dispaly problem solutions
def solution(request, problem_id):
    try:
        problem = Problem.objects.get(pk=problem_id)
    except Problem.DoesNotExist:
        raise Http404("problem does not exist")
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/solution.html',
        {
            'title':'Details',
            'problem': problem,
            'year':datetime.now().year,
        }
    )


#method to delete problem
def ProblemDelete(request, problem_id):
    try:
        problem = Problem.objects.get(pk=problem_id) # get problem with the id
        problem.delete()
    except Problem.DoesNotExist:
        raise Http404("problem does not exist")
    all_problems = Problem.objects.all()
    form = forms.SearchProblem
    print(all_problems)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/problems2.html',
        {
            'title': 'Problems',
            'all_problems': all_problems,
            'form': form,
            'year': datetime.now().year,
        }
    )


#method to creat new problem
class ProblemCreate(CreateView):
    model = Problem
    form_class = forms.ProblemForm

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


#method to creat new problem sets
class ProblemSetCreate(CreateView):
    model = ProblemSet
    form_class = forms.ProblemSetForm

    def get_success_url(self):
        return reverse('problemSet', args=(self.object.id,))


#method to update problem
def ProblemUpdate(request, problem_id):
    instance = get_object_or_404(Problem, id=problem_id)
    form = forms.ProblemForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('detail', pk=problem_id)
    return render(
        request,
        'app/problem_form.html',
        {
            'title': 'Update',
            'form': form,
            'year': datetime.now().year,
        }
    )


#method to update problem sets
def ProblemSetUpdate(request, problemset_id):
    instance = get_object_or_404(Problem, id=problemset_id)
    form = forms.ProblemSetForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('problemSet', pk=problemset_id)
    return render(
        request,
        'app/problemset_form.html',
        {
            'title': 'Update',
            'form': form,
            'year': datetime.now().year,
        }
    )



#method to delete problemsets
def ProblemSetDelete(request, problemset_id):
    try:
        problemset = ProblemSet.objects.get(pk=problemset_id)
        problemset.delete()
    except Problem.DoesNotExist:
        raise Http404("problem does not exist")
    Sets = ProblemSet.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/problems.html',
        {
            'title':'Problem Sets',
            'Sets': Sets,
            'year': datetime.now().year,
        }
    )


class UserFormView(View):
    form_class = UserForm
    template_name = 'app/registration_form.html'

    #new user registration
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,
                      {
                          'title' : 'Register',
                          'form': form,
                          'year': datetime.now().year,
                      }
        )

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name,
                      {
                          'title': 'Register',
                          'form': form,
                          'year': datetime.now().year,
                      }
        )