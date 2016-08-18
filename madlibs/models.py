from django.db import models



class Madlib(models.Model):
	"""
	Madlib definition, no blanks defined.
	
	A madlib object contains a text block and title defining it and a creation date.
	
	Attributes:
		text (str) -- text of the madlib, no blanks
		title (str) -- title description of madlib text
	"""
	text = models.TextField()
	title = models.CharField(max_length=32,primary_key=True)
	created_on = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		"""Return title as string for displaying instance."""
		return self.title
	def __unicode__(self):
		"""Return title as string for displaying instance."""
		return self.title
	
	def add_fields(self):
		pass
	
class Field(models.Model):
	"""Definition of a blank to replace a defined word in a specific madlib.
	
	A Field describes the blank and holds the filled word once entered by
	the user.
	
	Attributes:
		origin (str) -- original word to be replaces
		description (str) -- display description of word needed to replace the blank
		fill_in (str) -- the word added by the user
		part_of_speech (str) -- the part of speech of origin
		parent_title (str) -- title of the parent Madlib object
	
	"""
	origin = models.CharField(max_length=32)
	description = models.CharField(max_length=32,null=True)
	fill_in = models.CharField(max_length=32,null=True,blank=True)

	NOUN = 'Noun'
	PLURALNOUN = 'Plural Noun'
	ADJECTIVE = 'Adjective'
	ADVERB = 'Adverb'
	VERB = 'Verb'
	INGVERB = 'Verb ending with ing'
	
	POS_CHOICES = ((NOUN,'NN'),(PLURALNOUN,'NNS'),
				   (ADJECTIVE,'JJ'),(ADVERB,'RB'),
				   (VERB,'VB'),(INGVERB,'VBG'),)
	
	part_of_speech = models.CharField(max_length=16,
									 choices=POS_CHOICES,
									 null=True)
	parent_title = models.CharField(max_length=32)
	
	def __str__(self):
		"""Return title as string for displaying instance."""
		return '%s: %s'%(self.description, self.fill_in)
	def __unicode__(self):
		"""Return title as string for displaying instance."""
		return '%s: %s'%(self.description, self.fill_in)
	
	def is_filled(self):
		"""Check if blank has been filled."""
		return self.fill_in and self.fill_in!=''
	
	def add_word(self,word):
		"""Update object with word."""
		self.fill_in = word
		self.save()
		