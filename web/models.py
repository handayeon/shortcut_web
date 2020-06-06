from django.db import models

class Shortcut(models.Model):
    num = models.AutoField(db_column='num',blank=False,primary_key=True)
    os = models.CharField(db_column='os',max_length=200,blank=False)
    program = models.CharField(db_column='program',max_length=200,blank=False)
    action = models.CharField(db_column='action',max_length=300,blank=False)
    short = models.CharField(db_column='short',max_length=400,blank=False)

    class Meta:
        managed = False
        db_table = 'shortCut'

    def publish(self):
        self.save()

    def __str__(self):
        return "shortcut"

    