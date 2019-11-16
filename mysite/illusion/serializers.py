# from .models import History_db, Member_db, Reply_db, Style_db, Timeline_db, ContentImage, Preview
# from rest_framework import serializers
#
#
# class MemberSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Member_db
#         fields = ('url', 'user_num', 'user_id', 'password', 'gender', 'age', 'join_date', 'profile')
#
#
# class HistorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = History_db
#         fields = ('history_num', 'user_num', 'history_image_name', 'history_date', 'style_name', 'history_location')
#
#
# class TimelineSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Timeline_db
#         fields = ('time_num', 'user_num', 'upload_date', 'time_image_name', 'time_comment', 'time_location')
#
#
# class ReplySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Reply_db
#         fields = ('reply_num', 'time_num', 'user_num', 'reply_comment', 'reply_time')
#
#
# class StyleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Style_db
#         fields = ('style_num', 'style_name', 'style_path')
#
#
# class ContentImageSerializer(serializers.ModelSerializer):
#     path = serializers.FileField(required=False)
#
#     class Meta:
#         model = ContentImage
#         fields = '__all__'
#         read_only_filed = ('id', )
#
#
# class PreviewSerializer(serializers.ModelSerializer):
#     path = serializers.FileField(required=False)
#
#     class Meta:
#         model = Preview
#         fields = '__all__'
#         read_only_filed = ('id', )
