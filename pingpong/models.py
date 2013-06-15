from django.db import models
# Create your models here.
class User(models.Model):
    answear = models.BooleanField(default=True)
    first_name = models.CharField(blank=True, max_length=30, verbose_name='nom', )
    telephone = models.IntegerField(default=123456,verbose_name='telephone')
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.telephone)
    
    class Meta:
        ordering = ('first_name',)
        verbose_name_plural='users'

class Questions(models.Model):
    import datetime
    now = datetime.datetime.now()
    numero = models.AutoField(primary_key=True)
    question = models.CharField(max_length=300)
    release_date = models.DateField(default=now)
	
    def __unicode__(self):
        return u'%d %s' % (self.numero, self.question)
	
    class Meta:
        ordering = ('release_date',)
        verbose_name_plural = "questions"
        
class Responses(models.Model):
    import datetime
    now = datetime.datetime.now()
    response = models.CharField(max_length=300 )
    release_date = models.DateField(default=now)
    question = models.ForeignKey(Questions)
	
    def __unicode__(self):
        return u'%s' % (self.response)
	
    class Meta:
        ordering = ('release_date',)
        verbose_name_plural = "reponses"
		
class States(models.Model):
    num_tel = models.IntegerField(default=000000)
    n_messages = models.IntegerField(default=1)
    
    def __unicode__(self):
        return u'%s %s' % (self.num_tel, self.n_messages)
	
    class Meta:
        ordering = ('num_tel',)
        verbose_name_plural = "states"

class Ordre(models.Model):
    ordre = models.CharField(max_length=300, blank=True)
    num_poll = models.CharField(max_length=300, blank=True)
    def __unicode__(self):
        return u'%s %s' % (self.ordre, self.num_poll)
    class Meta:
        ordering = ('num_poll',)