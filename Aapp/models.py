# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from tinymce.models import HTMLField




MY_CHOICES = (
    ('GATE Preparation', 'GATE Preparation'),
    ('Thermodynamics', 'Thermodynamics'),
    ('Heat Transfer', 'Heat Transfer'),
	('Fluid mechanics', 'Fluid mechanics'),
    ('Strength of Materials', 'Strength of Materials'),
    ('UPSC ESE ME', 'UPSC ESE ME'),
	('Manufacturing Engineering', 'Manufacturing Engineering'),
    ('Engineering Design', 'Engineering Design'),
    ('Mechanics', 'Mechanics'),
	('Analytical Reasoning', 'Analytical Reasoning'),
    ('Industrial engineering', 'Industrial engineering'),
    ('Automotive technology', 'Automotive technology'),
	('Technology', 'Technology'),
    
)

class Blog(models.Model):
    
	title = models.CharField(max_length=100, unique=True)
	category = models.CharField(max_length=60,choices=MY_CHOICES)
	user = models.ForeignKey(User)
	Image = models.ImageField(upload_to='profile_image', blank=True)
	content = HTMLField(blank=True,default=0)


def __unicode__(self):
        return self.title

def get_absolute_url(self):
        return reverse('server_edit', kwargs={'pk': self.pk})
		
