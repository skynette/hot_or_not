from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hotvote(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	person = models.ForeignKey("Person", on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.user.username

class Notvote(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	person = models.ForeignKey("Person", on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.user.username
	

class Person(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	image = models.ImageField(blank=True, null=True)
	bio = models.TextField(max_length=100, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	hot_vote = models.IntegerField(default=0)
	not_vote = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username
	
	@property
	def hot_vote_count(self):
		return Hotvote.objects.filter(Person=self).count()
	@property
	def not_vote_count(self):
		return Notvote.objects.filter(Person=self).count()