from rest_framework import serializers
from jobs.models import Job , Application

## serializer for jobs ##
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

    ## method for update ##
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.responsibility = validated_data.get('responsibility',instance.responsibility)
        instance.experience = validated_data.get('experience',instance.experience)
        instance.benfits = validated_data.get('benfits',instance.benfits)
        instance.salary = validated_data.get('salary',instance.salary)
        # save instance #
        instance.save()
        return instance
    
    # method for creating #
    def create(self, validated_data):
        return Job.objects.create(**validated_data)


## serializer for application ##
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"

    ## method for update ##
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.responsibility = validated_data.get('responsibility',instance.responsibility)
        instance.experience = validated_data.get('experience',instance.experience)
        instance.benfits = validated_data.get('benfits',instance.benfits)
        instance.salary = validated_data.get('salary',instance.salary)
        # save instance #
        instance.save()
        return instance
    
    # method for creating #
    def create(self, validated_data):
        return Application.objects.create(**validated_data)

    ## method for validation ##
    def validate(self, data):
        if data['github_link'].startswith("https") and data['website_link'].startswith("https"):
            return data 
        raise serializers.ValidationError({"message":"github link or your website must starts with 'https'"})


