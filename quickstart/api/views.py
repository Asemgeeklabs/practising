from .serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from quickstart.models import Snippet

class SnippetListPost(APIView):
    ## list view ##
    def get(self,request):
        queryset = Snippet.objects.all()
        serializer = SnippetSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = SnippetSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"created successfully!","data":serializer.data},status=status.HTTP_201_CREATED)
        return Response({"message":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
    
### retrive update delete ###
class SnippetDetails(APIView):
    ## retrieve ##
    def get(self,request,id):
        snippet = Snippet.objects.get(id=id)
        serializer = SnippetSerializer(snippet)
        return Response({"data":serializer.data},status=status.HTTP_200_OK)
    ## update ##
    def put(self,request,id):
        ## object to be updated ##
        snippet = Snippet.objects.get(id=id)
        ## update using update built in method serializer ##
        serializer = SnippetSerializer(snippet,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response({"message":"notvalid"},status=status.HTTP_400_BAD_REQUEST)
    ## delete ##
    def delete(self,id,request):
        ## object to be updated ##
        try:
            snippet = Snippet.objects.delete(id=id)
            return Response({"message":"sbippet deleted successfully!"},status=status.HTTP_200_OK)
        except:
            return Response({"message":"sbippet not found"},status=status.HTTP_404_NOT_FOUND)


        

