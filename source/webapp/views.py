from django.shortcuts import render


# Create your views here.
def home_work(request):
    query = request.GET.getlist("name")
    cont = {"name": query}
    if request.method == "GET":
        return render(request, "index.html")
    else:
        # print(request.POST)
        f = request.POST.get("First")
        s = request.POST.get("Second")
        first = int(f)
        second = int(s)
        if request.POST.get("gridRadios") == "option1":
            result = first + second
            sign = "+"
        elif request.POST.get("gridRadios") == "option2":
            result = first - second
            sign = "-"
        elif request.POST.get("gridRadios") == "option3":
            result = first * second
            sign = "*"
        elif request.POST.get("gridRadios") == "option4":
            result = first / second
            sign = "/"
        context = {
            "grid": request.POST.get("gridRadios"),
            "result": result,
            "First": first,
            "Second": second,
            "Sign": sign
        }
    return render(request, "index.html", context)
