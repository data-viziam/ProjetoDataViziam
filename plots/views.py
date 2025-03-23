from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_plots(request):
    # Lógica para exibir os plots do usuário
    return render(request, 'plots/user_plots.html')