from django.shortcuts import render

import random
from random import randint

# Create your views here.
def index(request):
	roll = random.randint(1, 6)
	return render(request, "index.html", {"roll": roll})