from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question
from django.template import loader
from django.http import Http404
from django .core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.utils import timezone


'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
'''

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    f_question=get_object_or_404(Question,pk=1)
    context = {'latest_question_list': latest_question_list,'f_question':f_question,'user':request.user}
    return render(request, 'polls/index.html', context)



# Create your views here.
'''
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
'''

'''
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})   
'''

def detail(request, question_id):
    latest_question_list = Question.objects.order_by('-pub_date')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/index.html', {'f_question': question,'latest_question_list':latest_question_list,'user':request.user})     
    
'''
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
'''

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/index.html', {'question': question})  

def login_form(request):
    return render(request,'polls/login.html')    

def login_view(request):
    
    uname=request.POST['username']
    passd=request.POST['password']
    user=authenticate(username=uname,password=passd)
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect(reverse('polls:index'))        

            

                

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('polls:login_form'))  

def signup_view(request):
    uname=request.POST['username']
    passd=request.POST['password']
    email=request.POST['email']

    user = User.objects.create_user(uname, email, passd)
    user.first_name=request.POST['first_name']
    user.last_name=request.POST['last_name']
    user.save()
    return HttpResponseRedirect(reverse('polls:login_form'))  

def signup_form(request):
    return render(request,'polls/signup.html') 

def add_question(request):
    return render(request,'polls/add.html') 

def save_question(request):
    q_text=request.POST['question']
    c1=request.POST['choice1']
    c2=request.POST['choice2']
    c3=request.POST['choice3']

    q=Question(question_text=q_text,pub_date=timezone.now(),username=request.user.username)
    q.save()
    q.choice_set.create(choice_text=c1,votes=0)
    q.choice_set.create(choice_text=c2,votes=0)
    q.choice_set.create(choice_text=c3,votes=0)

    return HttpResponseRedirect(reverse('polls:add_question')) 







          




'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
'''
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))

def comment(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    cmn=""
    try:
        cmn = request.POST['comment']
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        c=question.comment_set.create(comment_text=cmn,user=request.user.username)
        c.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))        

