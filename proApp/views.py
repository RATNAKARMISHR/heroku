from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from commonfiles import response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import UserDetail
from .serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer,UserListSerilzer
from rest_framework import viewsets
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# class Record(viewsets.ModelViewSet):
#     def create(self,request,*args,**kwargs):
#         serializer=self.UserSerializer(data=request.data)
#         self.perform_create(serializer)
     #   return JsonResponse(response.Success("added",serializer.data))
class List(generics.ListAPIView):
    queryset=UserDetail.objects.all()
    serializer_class=UserListSerilzer


class DeleteUser(generics.DestroyAPIView):
    queryset=UserDetail.objects.all()
    serializer_class=UserSerializer

    # def get(self,request):
    #     serializer_class=UserListSerilzer(request.data)
    #     return JsonResponse(response.Success("list is created",serializer_class.data))

class Record(generics.ListCreateAPIView):
    # get method handler
   queryset = UserDetail.objects.all()
   serializer_class = UserSerializer
   

# class Record(APIView):
#     def post(self,request):

#         serializer=UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             #return Response(serializer.data,status=status.HTTP_201_CREATED)
#             return JsonResponse(response.Success("User Added",serializer.data))
#         #return Response(serializer,errors,status=status.HTTP_400_BAD_REQUEST)
#         return JsonResponse(response.Failure("user not added"))

    #def data():

    # def post(self,request,*args,**kwargs):
    #     serializer_class=UserSerializer(data=request.data)
    #     if serializer_class.is_valid(raise_exception=True):
    #         return JsonResponse(response.Success("User Added Sucessfully",serializer_class.data))
    #     else:
    #         return JsonResponse(response.Failure("User is not added"))



'''
class UserDetail(APIView):
    def get(self,request,pk):
        try:
            return JsonResponse(response.Success("user details",User.objects.get(pk=pk))
        except Exception as e:

            raise JsonResponse(response.Failure())
        '''



#class RecordDelete(generics.)
class update(generics.UpdateAPIView):
    queryset=UserDetail.objects.all()
    serializer_class=UserSerializer

class RecordUpdate(generics.RetrieveAPIView):
    queryset=UserDetail.objects.all()
    serializer_class=UserListSerilzer
    # def post(self,request,*args,**kwargs):
    #     serializer_class=UserSerializer(data=request.data)
    #     if serializer_class.is_valid(raise_exception=True):
    #         return JsonResponse(response.Success("record Updated sucessfully",serializer_class.data))
    #     else:
    #         return JsonResponse(response.Failure("Not Updated"))

class Login(generics.GenericAPIView):
    # get method handler
    queryset = UserDetail.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
           
           
            
            #return Response(serializer_class.data, status=HTTP_200_OK)
            return JsonResponse(response.Success("logged In sucessfully",serializer_class.data))
        #return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)
        return JsonResponse(response.Failure("not able to loggedIn"))


class Logout(generics.GenericAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            #return Response(serializer_class.data, status=HTTP_200_OK)
            return JsonResponse(response.Success("loggedout"))
        #return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)
        return JsonResponse(response.Failure("Invalid Request"))




def index(request):
    return redirect('/api/login')