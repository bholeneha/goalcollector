from django.shortcuts import render
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Goal:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, reason, what, deadline):
    self.name = name
    self.reason = reason
    self.what = what
    self.deadline = deadline

goals = [
  Goal('Read', 'Gain perspective', 'Read 10 mins a day', 'Everyday'),
  Goal('Save for Europe Trip', 'I want to see Italy', 'Save $5000', '2 months'),
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Welcome to Goal Collector</h1>')

def about(request):
  return render(request, 'about.html')

def goals_index(request):
  return render(request, 'goals/index.html', { "goals": goals })