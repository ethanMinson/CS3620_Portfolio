from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Madlib
from .form import MadLibForm

from .models import Madlib

# Create your views here.
def index(request):
    madlib_list = Madlib.objects.all()
    context = {"madlib_list": madlib_list}
    return render(request, 'index.html', context)

def madlib(request, slug):
    story = Madlib.objects.get(slug=slug)

    if request.method == "POST":
        form = MadLibForm(story.blanks, request.POST)
        if form.is_valid():
            filled_values = [form.cleaned_data[f"blank_{i}"] for i in range(len(story.blanks))]
            # Combine clips and filled values into a final story
            result = "".join(
                part + (filled_values[i] if i < len(filled_values) else "")
                for i, part in enumerate(story.story_clips)
            )
            return render(request, "your_story.html", {"story": story, "result": result})
    else:
        form = MadLibForm(story.blanks)

    return render(request, "madlib.html", {"story": story, "form": form})

