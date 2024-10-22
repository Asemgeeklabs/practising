from rest_framework import generics , mixins , views , response
from jobs.models import Job , Application
from .serializers import JobSerializer , ApplicationSerializer

### endpoint to post a nd list jobs ###
class JobListPost(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    ## list jobs ##
    def get(self, request , *args , **kwargs):
        return self.list(request , *args , **kwargs)

    ## create (post) jobs ##
    def post(self, request , *args , **kwargs):
        return self.create(request , *args , **kwargs)

## retrive update delete job ##
class JobDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

### endpoint to post a nd list applications ###
class ApplicationList(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

### endpoint to post a nd list applications ###
class ApplicationPost(generics.GenericAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def post(self,request,id):
        job = Job.objects.get(id=id)
        data = request.data.copy()
        data["job"] = job.pk
        serializer = ApplicationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors)
    
# class TestRelated(views.APIView):
#     def get(self, request):
#         queryset = Application.objects.select_related("job")
#         serializer = ApplicationSerializer(queryset,many=True)
#         return response(serializer.data)


