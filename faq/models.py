from django.db import models


class FaqCategory(models.Model):
    """
    FAQ categories
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Faq(models.Model):
    """
    FAQ information
    Related to (FK) :FaqCategory
    """
    category = models.ForeignKey(
        'FaqCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    question = models.CharField(max_length=255, null=False, blank=False)
    answer = models.TextField(max_length=2000, null=False, blank=False)

    def __str__(self):
        return self.question
