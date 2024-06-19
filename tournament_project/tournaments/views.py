from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Tournament
from .forms import TournamentForm

def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournaments/tournament_list.html', {'tournaments': tournaments})

def tournament_detail(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    return render(request, 'tournaments/tournament_detail.html', {'tournament': tournament})

def tournament_create(request):
    if request.method == "POST":
        form = TournamentForm(request.POST)
        if form.is_valid():
            tournament = form.save()
            return redirect('tournament_detail', pk=tournament.pk)
    else:
        form = TournamentForm()
    return render(request, 'tournaments/tournament_form.html', {'form': form})

def tournament_update(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == "POST":
        form = TournamentForm(request.POST, instance=tournament)
        if form.is_valid():
            tournament = form.save()
            return redirect('tournament_detail', pk=tournament.pk)
    else:
        form = TournamentForm(instance=tournament)
    return render(request, 'tournaments/tournament_form.html', {'form': form})

def tournament_delete(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == 'POST':
        tournament.delete()
        return redirect('tournament_list')
    return render(request, 'tournaments/tournament_confirm_delete.html', {'tournament': tournament})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
