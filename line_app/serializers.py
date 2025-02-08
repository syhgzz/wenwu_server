from rest_framework import serializers
# 在序列化器中导入用户的ORM模型
from line_app.models import Film
from line_app.models import Performer
from line_app.models import Type
class Performerserializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = '__all__'
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Type
        fields = '__all__'
class FilmSerializer(serializers.ModelSerializer):
    per = Performerserializer(source='performer')
    type = TypeSerializer(source='film_type')
    class Meta:
        model = Film
        fields = ('id', 'film_name', 'time', 'film_url', 'desc', 'per', 'type')
 
