# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    pass


class Collection(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Question(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
