from django.db import models

class Stock(models.Model):
    """Stock model."""

    name = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255)
    id = models.CharField(max_length=255, primary_key=True)

    def __str__(self) -> str:
        """Return name."""
        return self.name