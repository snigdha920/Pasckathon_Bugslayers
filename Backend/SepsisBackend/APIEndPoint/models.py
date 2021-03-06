from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Patients(models.Model):

    patient_id = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)

    hosp = models.ForeignKey(User, on_delete=models.CASCADE)

    hr = models.FloatField()
    o2sat = models.FloatField()
    temp = models.FloatField()
    sbp = models.FloatField()
    map = models.FloatField()
    dbp = models.FloatField()
    resp = models.FloatField()
    etco2 = models.FloatField()

    baseexcess = models.FloatField()
    hco3 = models.FloatField()
    fio2 = models.FloatField()
    ph = models.FloatField()
    paco2 = models.FloatField()
    sao2 = models.FloatField()
    ast = models.FloatField()
    bun = models.FloatField()
    alkalinephos = models.FloatField()
    calcium = models.FloatField()
    chloride = models.FloatField()
    creatinine = models.FloatField()
    bilirubin_direct = models.FloatField()
    glucose = models.FloatField()
    lactate = models.FloatField()
    magnesium = models.FloatField()
    phosphate = models.FloatField()
    potassium = models.FloatField()
    bilirubin_total = models.FloatField()
    troponini = models.FloatField()
    hct = models.FloatField()
    hgb = models.FloatField()
    ptt = models.FloatField()
    wbc = models.FloatField()
    fibrinogen = models.FloatField()
    platelets = models.FloatField()

    age = models.FloatField()
    gender = models.FloatField()
    hospadmtime = models.FloatField()
    iculos = models.FloatField()

    sepsislabel = models.FloatField(default=0.0)
