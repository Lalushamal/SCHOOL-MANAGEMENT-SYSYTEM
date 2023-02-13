from django.db import models

GENDER=[ 
    ('male','Male'),
    ('female','Female'),
    ('transegender','transegender'),
]
MONTH=[ 
    ('january','january'),
    ('february','february'),
    ('march','march'),
    ('april','april'),
    ('may','may'),
    ('june','june'),
    ('july','july'),
    ('august','august'),
    ('september','september'),
    ('october','october'),
    ('november','november'),
    ('december','december'),
]


BATCH_TIME=[ 
    ('9-12','9-12'),
    ('12-2','12-2'),
    ('2-5','2-5'),
]

class Course(models.Model):
    course=models.CharField(max_length=100)
    def __str__(self):
        return str(self.course)

class Register(models.Model):
    register_no=models.IntegerField(unique=True, blank=False)
    name=models.CharField(max_length=100)
    address=models.TextField()
    age=models.IntegerField()
    gender=models.TextField(choices=GENDER)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch_time=models.TextField(choices=BATCH_TIME)
    phone_no=models.IntegerField()
    email=models.TextField(max_length=30)
    def __str__(self):
        return str(self.name)
class Attendences(models.Model):
    register_no=models.IntegerField()
    year=models.IntegerField()
    month=models.TextField(choices=MONTH)
    present=models.IntegerField()
    absent=models.IntegerField()
class Mark(models.Model):
    register_no=models.IntegerField()
    exam_date=models.DateField()
    mark_theory=models.IntegerField()
    mark_pratical=models.IntegerField()
    
class Attend(models.Model):
    register_no=models.IntegerField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    month=models.ForeignKey(Attendences,on_delete=models.CASCADE)
    year=models.IntegerField()
    

    


    
