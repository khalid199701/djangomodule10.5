from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'author': 'Rahim', 'num_cherries' : 2, 'birthday': datetime.datetime.now(), 'age' : 30, 'lst': ['1','2', '3'], 'courses':[
        {
            'id': 1,
            'course':'python',
            'fee' : 1000
        },
        {
            'id': 2,
            'course':'django',
            'fee' : 10000
        },
        {
            'id': 3,
            'course':'cpp',
            'fee' : 1500
        }
    ]}
    return render(request, 'home.html', context=d)