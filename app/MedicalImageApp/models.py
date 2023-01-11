from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class UserInformation(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    STATUS_CHOICES = [
        (MALE, 'male'),
        (FEMALE, 'female')
    ]
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    middle_name = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=6,
        choices=STATUS_CHOICES,
        null=False,
        blank=False
    )
    date_of_birth = models.DateField(
        null=False,
        blank=False,
        help_text='Set Your Date of Birth'
    )


class Doctor(models.Model):
    user = models.ForeignKey(
        UserInformation,
        on_delete=models.CASCADE
    )
    medical_specialty = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='max character is approve is 100 character, be careful '
    )


class Patient(models.Model):
    user = models.ForeignKey(
        UserInformation,
        on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )
    patient_history = models.TextField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Add any patient history, max length is 255 character'
    )
    visit_date = models.DateTimeField(
        help_text='date of patient visit the doctor',
        default=now,
        null=False,
        blank=False,
    )


class MedicalImage(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )
    medical_image = models.ImageField(
        verbose_name='Medical Image of the patient',
        name="Medical Image",
        width_field=100,
        height_field=100,
        upload_to='medical_image',
        null=True,
        blank=True
    )
    cypher = models.JSONField(
        verbose_name="cypher",
        name="Cypher",
        default="",
        null=False,
        blank=False
    )
    h_cypher = models.JSONField(
        verbose_name='hash of cypher',
        name='cipher + Hash',
        default="",
        null=False,
        blank=False
    )
    Description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
    )
