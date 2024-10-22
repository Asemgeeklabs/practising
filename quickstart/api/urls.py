from django.urls import path 
from .views import SnippetListPost , SnippetDetails
from .viewsMixins import SnippetListCreate , SnippetMixinsDetails

urlpatterns = [
    path('snippets/', SnippetListPost.as_view()),
    path('snippets/<int:id>/', SnippetDetails.as_view()),
    path('snippets/mixins/', SnippetListCreate.as_view()),
    path('snippets/mixins/<int:pk>/', SnippetMixinsDetails.as_view()),
]