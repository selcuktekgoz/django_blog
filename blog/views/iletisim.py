from django.shortcuts import render


def iletisim(request):
    context = {"sayfa": "iletişim"}
    return render(request, "pages/iletisim.html", context)
