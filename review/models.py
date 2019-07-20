from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    Cname = models.CharField(max_length=100)
    Cid = models.IntegerField(primary_key=True)

    def __str__(self):
        # return '{}/{}'.format(self.Cname,self.Cid)
        return self.Cname


class Restaurant(models.Model):
    Cid = models.ForeignKey(Category,db_column='Cid', on_delete=models.Aggregate)
    Rname = models.CharField(max_length=200)
    Rid = models.IntegerField(primary_key=True)
    Radd=models.CharField(max_length=300)
    Rimage=models.CharField(max_length=300, null=True)
    Rdesc=models.CharField(max_length=300, null=True)

    def __str__(self):
        return '{}/{}/{}/{}/{}/{}'.format(self.Rid,self.Rname,self.Radd,self.Cid,self.Rimage,self.Rdesc)
       # return self.Rid

class Review(models.Model):
    Rvname = models.CharField(max_length=200)
    Rvid = models.IntegerField(primary_key=True)
    Rating = models.IntegerField(default=0)
    Rid = models.ForeignKey(Restaurant,db_column='Rid',on_delete=models.Aggregate)

    def __str__(self):
        return '{}/{}/{}/{}'.format(self.Rvid,self.Rvname,self.Rating,self.Rid)

class Comment(models.Model):
    Comid = models.IntegerField(primary_key=True)
    Ce_text = models.CharField(max_length=200)
    Rvid= models.ForeignKey(Review,db_column='Rvid',on_delete=models.Aggregate)

    def __str__(self):
        return '{}/{}/{}'.format(self.Comid,self.Ce_text,self.Rvid)

