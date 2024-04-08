from django.views.generic import DetailView, ListView

from blogi.models import Postaus


class PostausListaNäkymä(ListView):
    model = Postaus


class PostausNäytäNäkymä(DetailView)
    model = Postaus
