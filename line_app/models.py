from django.db import models

# Create your models here.
from rest_framework.permissions import IsAuthenticated
# Create your models here.
class Performer(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'performer'
class Type(models.Model):
    type = models.CharField(max_length=20)
    def __str__(self):
        return self.type
    class Meta:
        db_table='type'
class Film(models.Model):
    film_name = models.CharField(max_length=50,null=False)
    performer = models.ForeignKey(Performer,on_delete=models.CASCADE)
    film_type = models.ForeignKey(Type,on_delete=models.CASCADE)
    time = models.DateField()
    film_url = models.URLField()
    desc = models.TextField()
    def __str__(self):
        return self.film_name+'_'+str(self.performer)
    class Meta:
        db_table = 'Film'


class File(models.Model):
    upload_file = models.FileField(upload_to='./upload')
    processed_file = models.FileField(upload_to='./processed')

    def __str__(self):
        return self.upload_file.name
 
    class Meta:
        db_table = 'file'               