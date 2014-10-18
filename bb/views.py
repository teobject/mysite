from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from bb.models import BB
from bb.forms import BBForm

def index(request):
    all_comment = BB.objects.all()
    return direct_to_template(request, 'bb/index.html',
            {'all_comment': all_comment, 'form': BBForm()})

def post(request):
    if request.method != 'POST':
        return redirect('/bb/')

    form = BBForm(request.POST)
    if form.is_valid():
        bb = BB()
        bb.title = form.cleaned_data['title']
        bb.name = form.cleaned_data['name']
        bb.comment = form.cleaned_data['comment']
        bb.save()

    dict = {'form': form}
    dict['all_comment'] = BB.objects.all()
    return direct_to_template(request, 'bb/index.html', dict)
