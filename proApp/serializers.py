from django.db.models import Q # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import UserDetail
from django.core.exceptions import ValidationError
#from uuid import uuid4
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from commonfiles import response
from django.http.response import JsonResponse
from commonfiles.count import count


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    access=AccessToken.for_user(user)
    return str(refresh.access_token)

# c=0
# def increment_role_id():
#     global c
#     c=count(c)
#     new_role_id='U'+'000'+str(c)
#     return str(new_role_id)


class UserListSerilzer(serializers.ModelSerializer):

    email = serializers.EmailField(required=False,validators=[UniqueValidator(queryset=UserDetail.objects.all())],read_only=True)
    role=serializers.CharField(max_length=10,read_only=True)
    id=serializers.CharField(max_length=10,read_only=True)
    City=serializers.CharField(max_length=10,read_only=True)
    Gender=serializers.CharField(max_length=2,read_only=True)
    mobile_No=serializers.CharField(max_length=10,read_only=True)
    Firstname=serializers.CharField(max_length=20,read_only=True)
    Middlename=serializers.CharField(max_length=20,read_only=True)
    Lastname=serializers.CharField(max_length=20,read_only=True)
    State=serializers.CharField(max_length=20,read_only=True)
    zipcode=serializers.CharField(max_length=6,read_only=True)

    
    class Meta:
        model = UserDetail
        fields = (
            'role',
            'id',
            'Firstname',
            'Middlename',
            'Lastname',
            #'Username',
            'email',
            #'password',
            'Gender',
            'mobile_No',
            'City',
            'State',
            'zipcode',
        )


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=UserDetail.objects.all())],write_only=True)
    Username = serializers.CharField(required=True,validators=[UniqueValidator(queryset=UserDetail.objects.all())],write_only=True)
    #Iden=serializers.CharField(max_length=10,default=increment_role_id,required=False,read_only=True)
    password = serializers.CharField(max_length=8,write_only=True)
    role=serializers.CharField(max_length=10,write_only=True)
    City=serializers.CharField(max_length=10,write_only=True)
    Gender=serializers.CharField(max_length=2,write_only=True)
    mobile_No=serializers.CharField(max_length=10,write_only=True)
    Firstname=serializers.CharField(max_length=20,write_only=True)
    Middlename=serializers.CharField(max_length=20,write_only=True)
    Lastname=serializers.CharField(max_length=20,write_only=True)
    State=serializers.CharField(max_length=20,write_only=True)
    zipcode=serializers.CharField(max_length=6,write_only=True)

    
    class Meta:
        model = UserDetail
        fields = (
            'role',
            #'id',
            'Firstname',
            'Middlename',
            'Lastname',
            'Username',
            'email',
            'password',
            'Gender',
            'mobile_No',
            'City',
            'State',
            'zipcode',
        )


class UserLoginSerializer(serializers.ModelSerializer):
    # to accept either username or email
    #role=serializers.CharField()
    Username = serializers.CharField()
    password = serializers.CharField()
    id=serializers.CharField(required=False,read_only=True)
    token = serializers.CharField(required=False, read_only=True)
    role=serializers.CharField(read_only=True,required=False)
    City=serializers.CharField(max_length=10,read_only=True)
    Gender=serializers.CharField(max_length=2,read_only=True)
    mobile_No=serializers.CharField(max_length=10,read_only=True)
    Firstname=serializers.CharField(read_only=True)
    Middlename=serializers.CharField(read_only=True)
    Lastname=serializers.CharField(max_length=20,read_only=True)
    State=serializers.CharField(max_length=20,read_only=True)
    zipcode=serializers.CharField(max_length=6,read_only=True)


    def validate(self, data):
        # user,email,password validator
        Username = data.get("Username", None)
        password = data.get("password", None)
        #role=data.get("role",None)
        if not Username and not password:
            #raise ValidationError("Details not entered.")
            raise ValidationError(response.Failure("details not enterned"))
        user = None
        # if the email has been passed
        if '@' in Username:
            user = UserDetail.objects.filter(
                Q(email=Username) &
                Q(password=password)
                ).distinct()
            if not user.exists():
                #raise ValidationError("User credentials are not correct.")
                raise ValidationError(response.Failure("wrong username or psd"))
            user = UserDetail.objects.get(email=Username)
        else:
            user = UserDetail.objects.filter(
                Q(Username=Username) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                #raise ValidationError("User credentials are not correct.")
                raise ValidationError(response.Failure("wrong user name or password"))
            user = UserDetail.objects.get(Username=Username)
        if user.ifLogged:
            pass
            #raise ValidationError("User already logged in.")
        user.ifLogged = True
        data['token'] = get_tokens_for_user(user)
        user.token = data['token']
        data['role']=user.role
        data['id']=user.id
        data['Firstname']=user.Firstname
        data['Middlename']=user.Middlename
        data['Lastname']=user.Lastname
        data['mobile_No']=user.mobile_No
        data['Gender']=user.Gender
        data['City']=user.City
        user.save()
        return data

    class Meta:
        model = UserDetail
        fields = (
            'id',
            'Username',
            'password',
            'role',
            'Firstname',
            'Middlename',
            'Lastname',
            'City',
            'State',
            'mobile_No',
            'zipcode',
            'Gender',
            'token',


            #'token',
            
        )

        read_only_fields = (
            'token',
            
        )







class UserLogoutSerializer(serializers.ModelSerializer):
    Username = serializers.CharField()
    status = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        #token = data.get("token", None)
        Username=data.get("Username",None)
        #print(username)
        user = None
        try:
            user = UserDetail.objects.get(Username=Username)
            if not user.ifLogged:
                #raise ValidationError("User is not logged in.")
                raise ValidationError(response.Failure("User is not Logged In"))
        except Exception as e:
            raise ValidationError(str(e))
        user.ifLogged = False
        #user.token = ""
        user.save()
        data['status'] = "User is logged out."
        return JsonResponse(response.Success("succesfully Logged Out"))

    class Meta:
        model = UserDetail
        fields = (
            'Username',
            'status',
        )
