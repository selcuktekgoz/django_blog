from django.shortcuts import render


def anasayfa(request):
    context = {"sayfa": "anasayfa"}
    return render(request, "pages/anasayfa.html", context)
