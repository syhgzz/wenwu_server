import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wenwu_server.settings")# untitled 项目名称
django.setup()
from line_app.models import Film,Type,Performer
from line_app.serializers import *
 
movies=Film.objects.all()
# print(movies,type(movies))
# movie_values = movies.values()
# film_list = list(movie_values)
# print(film_list,type(film_list))

film_list_serial = FilmSerializer(movies,many=True)
print(film_list_serial.data)