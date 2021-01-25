'''
import django_tables2 as tables
from .models import Details
import itertools

class ProjectTable(tables.Table):
    class Meta:
       model = Details
       template_name = "django_tables2/bootstrap.html"
       reporttype = tables.Column("reporttype")
       transactionid = tables.Column("transactionid")
       submitdate = tables.Column("submitdate")
       claim = tables.Column("claim")
       score = tables.Column("score")
       predictiondate = tables.Column("predictiondate")
       manualintervention = tables.Column("manualintervention")
       formerlynomi = tables.Column("formerlynomi")
'''