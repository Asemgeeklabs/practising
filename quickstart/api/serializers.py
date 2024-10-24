## serializer for users and groups ##
from rest_framework import serializers
from quickstart.models import Snippet , LANGUAGE_CHOICES , STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    title= serializers.CharField(required=True,allow_blank=True,max_length=100)
    code = serializers.CharField(style={"base_template":"textarea_html"})
    linenos = serializers.BooleanField(default=True)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')
    password = serializers.CharField(style={"input_type":"password","placeholder":"enter your password"})

    ### built in methods in serializer ###
    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.code = validated_data.get('code',instance.code)
        instance.linenos = validated_data.get('linenos',instance.linenos)
        instance.language = validated_data.get('language',instance.language)
        instance.style = validated_data.get('style',instance.style)
        instance.password = validated_data.get('password',instance.password)
        instance.save()
        return instance

    
