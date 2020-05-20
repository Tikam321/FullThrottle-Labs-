from rest_framework import serializers
from .models import Time_Period,User_Name


class Time_PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_Period
        fields = [ 'start_time', 'end_time']


class User_NameSerializer(serializers.ModelSerializer):
    activity_periods = Time_PeriodSerializer(many=True, read_only=True)


    class Meta:
        model = User_Name
        fields = ['id','timezone','real_name','activity_periods']
