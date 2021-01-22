from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length = 1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

class Details(models.Model):
    reporttype = models.CharField(db_column='ReportType', max_length=5, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.TextField(db_column='TransactionID', blank=True, null=True)  # Field name made lowercase.
    submitdate = models.DateField(db_column='SubmitDate', blank=True, null=True)  # Field name made lowercase.
    claim = models.FloatField(db_column='Claim', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    predictiondate = models.DateField(db_column='PredictionDate', blank=True, null=True)  # Field name made lowercase.
    manualintervention = models.CharField(db_column='ManualIntervention', max_length=3, blank=True, null=True)  # Field name made lowercase.
    formerlynomi = models.CharField(db_column='FormerlyNoMI', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'details'

