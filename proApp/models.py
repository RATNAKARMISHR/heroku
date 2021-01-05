from django.db import models
from commonfiles.count import count
# Create your models here.


    # class Meta:
    #     managed = Truefrom django.db import models
c=0
def increment_role_id():
    global c
    c=count(c)
    new_role_id='U-'+'00'+str(c)
    return str(new_role_id)



class UserDetail(models.Model):

    id =models.CharField(max_length=25,primary_key=True,default=increment_role_id)
    Firstname=models.CharField(max_length=20,default='')
    Middlename=models.CharField(max_length=20,default='',blank=True)
    Lastname = models.CharField(max_length=255, default='')
    Username=models.CharField(max_length=20)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=50)
    ifLogged = models.BooleanField(default=False)
    role=models.CharField(max_length=10,null=False,default="")
    mobile_No=models.CharField(max_length=10,default="")
    Gender=models.CharField(max_length=2,default="")
    City=models.CharField(max_length=10,default="")
    State=models.CharField(max_length=20,default="")
    zipcode=models.CharField(max_length=6,default="")
    
   
    #     db_table = "Role"
   