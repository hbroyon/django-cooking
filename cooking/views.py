# -*- coding: utf-8 -*-
from django.views import generic

from cooking.models import Recipe


# Create your views here.
class IndexView(generic.ListView):
    """
    The main view.
    """
    model = Recipe
    template_name = "cooking/index.html"
    pk_url_kwarg = 'id'
