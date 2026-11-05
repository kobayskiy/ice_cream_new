from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContestForm
from .models import Contest

def proposal(request):
    form = ContestForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        contest = form.save()
        context['contest_id'] = contest.id

    return render(request, 'contest/form.html', context=context)

def proposal_list(request):
    contests = Contest.objects.order_by('id')
    context = {'contests': contests}
    return render(request, 'contest/list.html', context=context)

def proposal_edit(request, pk):
    contest = get_object_or_404(Contest, pk=pk)
    form = ContestForm(request.POST or None, instance=contest)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('contest:list')

    context = {'form': form, 'contest': contest}
    return render(request, 'contest/form.html', context=context)

def proposal_delete(request, pk):
    contest = get_object_or_404(Contest, pk=pk)

    if request.method == 'POST':
        contest.delete()
        return redirect('contest:list')

    context = {'contest': contest}
    return render(request, 'contest/form.html', context=context)