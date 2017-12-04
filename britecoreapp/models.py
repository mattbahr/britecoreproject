from django.db import models

class RiskType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RiskTypeField(models.Model):
    TEXT = 'TEXT'
    NUMBER = 'NUMBER'
    DATE = 'DATE'
    ENUM = 'ENUM'
    TYPE_CHOICES = (
        (TEXT, 'Text'),
        (NUMBER, 'Number'),
        (DATE, 'Date'),
        (ENUM, 'Enum'),
    )
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    field_type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
        default=TEXT,
    )

    def __str__(self):
        return self.name

class RiskTypeFieldOption(models.Model):
    risk_type_field = models.ForeignKey(
        RiskTypeField,
        on_delete=models.CASCADE,
        limit_choices_to={'field_type': RiskTypeField.ENUM},
    )
    option_text = models.CharField(max_length=200)

    def __str__(self):
        return self.option_text
