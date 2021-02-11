from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views

from django.shortcuts import get_object_or_404

from .models import Article
from .serializers import ArticleSerializer

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins

from rest_framework.authentication import SessionAuthentication,BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated 

from rest_framework import viewsets

# Create your views here.

# model view sets
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


# generic view sets
# can perform similar fns as view sets
# class ArticleViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()


# view sets

# class ArticleViewSet(viewsets.ViewSet):
#     def list(self,request):
#         articles=Article.objects.all()
#         serializer=ArticleSerializer(articles,many=True)
#         return Response(serializer.data)
#     def create(self,request):
#         serializer=ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def retrieve(self,request,pk=None):
#         queryset=Article.objects.all()
#         article=get_object_or_404(queryset,pk=pk)
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data)
#     def update(self,request,pk=None):
#         article=Article.objects.get(pk=pk)
#         serializer=ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # similarly delete

# generic views

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'

    # auth config => first check if session auth avalilable or use the basic auth
    # authentication_classes=[SessionAuthentication,BasicAuthentication]

    # token auth
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, request, id = None): 
        if id:
            return self.retrieve(request)
        else:
           return self.list(request)
    def post(self, request):
        return self.create(request)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id):
        return self.destroy(request, id)

# class based views

class ArticleAPIView(APIView):
    def get(self,request):
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleAPIDetailsView(APIView):
    def get_object(self,id):
        try:
            article=Article.objects.get(id=id)
            return article
        except Article.DoesNotExist:  
            return Response(staus=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        article=self.get_object(id)
        serializer=ArticleSerializer(article)
        return Response(serializer.data)
    def put(self,request,id):
        article=self.get_object(id)
        serializer=ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        article=self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# function based

# @csrf_exempt
# def article_list(request):
#     if request.method=='GET':
#         articles=Article.objects.all()
#         serializer=ArticleSerializer(articles,many=True)
#         return JsonResponse(serializer.data,safe=False)

#     elif request.method=='POST':
#         data=JSONParser().parse(request)
#         serializer=ArticleSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)

# @csrf_exempt
# def article_detail(request,pk):
#     # try to get article
#     try:
#         article=Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(staus=404)
    
#     if request.method=='GET':
#         serializer=ArticleSerializer(article)
#         return JsonResponse(serializer.data)
#     elif request.method=='PUT':
#         data=JSONParser().parse(request)
#         serializer=ArticleSerializer(article,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors,status=400)
#     elif request.method=='DELETE':
#         article.delete()
#         return HttpResponse(status=204)

# @api_view(['GET','POST'])
# def article_list(request):
#     if request.method=='GET':
#         articles=Article.objects.all()
#         serializer=ArticleSerializer(articles,many=True)
#         return Response(serializer.data)

#     elif request.method=='POST':
#         serializer=ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def article_detail(request,pk):
#     try:
#         article=Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(staus=status.HTTP_404_NOT_FOUND)
    
#     if request.method=='GET':
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data)
#     elif request.method=='PUT':
#         serializer=ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=='DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

