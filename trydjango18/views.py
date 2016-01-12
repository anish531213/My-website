from django.shortcuts import render


def about(request):
	return render(request, "about.html", {})
def about2(request):
	return render(request, "about2.html", {})

def maintainence(request):
	return render(request, "maintainence.html", {})
def comparison(request):
	return render(request, "Comparison.html", {})

