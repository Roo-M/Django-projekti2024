from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostausListaNäkymä.as_view(),
         name="postaus-lista",
    ),
    path("<int:pk>/",
         views.PostausNäytäNäkymä.as_view(),
         name="postaus-näytä",
    ),

]

