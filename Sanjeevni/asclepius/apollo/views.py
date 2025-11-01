from django.shortcuts import render, redirect
from .forms import ReportForm
from django.http import HttpResponse

def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            print(request.user)
            form.save({'user':request.user})
            return redirect('report-success/')  # or another page
    else:
        form = ReportForm()
    
    return render(request, 'create_report.html', {'form': form,'user':request.user})

def report_success(request):
    return HttpResponse("yay")
