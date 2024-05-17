from django.shortcuts import render

# Create your views here.


def counter(request):
    data = ''
    if request.method == 'POST':
        words = request.POST['words']
        select = request.POST['select']
        if select == 'letter':
            data = f"{len(words)} herf"
        else:
            data = f"{len(words.split())} soz"
    context = {
        'data': data
    }
    return render(request, 'counter.html', context)

        

