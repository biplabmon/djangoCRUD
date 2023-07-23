from rest_framework import serializers
from book_api.models import Book


# -------- SERIALIZER FOR FUNCTION BASE VIEWS (REST API) --------
# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     number_of_pages = serializers.IntegerField()
#     publish_date = serializers.DateField()
#     quantity = serializers.IntegerField()
    
#     def create(self, data):
#         return Book.objects.create(**data)
    
#     def update(self, instence, data):
#         instence.title = data.get('title', instence.title)
#         instence.number_of_pages = data.get('number_of_pages', instence.number_of_pages)
#         instence.publish_date = data.get('publish_date', instence.publish_date)
#         instence.quantity = data.get('quantity', instence.quantity)
#         instence.save()
#         return instence

# -------- SERIALIZER FOR CLASS BASE VIEWS (REST API) --------
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"