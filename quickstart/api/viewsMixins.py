from quickstart.models import Snippet
from rest_framework import mixins , generics
from .serializers import SnippetSerializer

## endpoint to list and create snippet ##
class SnippetListCreate(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    ## main attributes ##
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    ## for list ##
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    ## for create ##
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SnippetMixinsDetails(generics.GenericAPIView,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin):
    ## main attributes ##
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # for retrieve #
    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    # update #
    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    # delete # 
    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)