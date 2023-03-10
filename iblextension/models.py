"""
Database models for ibl_app.
"""
from django.db import models


class Greeting(models.Model):
    """
    TODO: replace with a brief description of the model.

    TODO: Add either a negative or a positive PII annotation to the end of this docstring.  For more
    information, see OEP-30:
    https://open-edx-proposals.readthedocs.io/en/latest/oep-0030-arch-pii-markup-and-auditing.html
    """

    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for Greeting.
        """

        ordering = ['-created_at']
        verbose_name_plural = 'Greetings'


    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return self.text
    

