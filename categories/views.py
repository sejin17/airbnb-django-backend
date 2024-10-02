from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Category
#to serialize querymap to json
from .serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet

class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    queryset = Category.objects.filter(
        type=Category.CategoryKindChoices.ROOM,
    )
"""
# GET /categories
@api_view(["GET", "POST"]) # allowing get and post methods
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True) # if without many option, CategorySerializer can only serialize one field 
        return(
            {
                "ok": True,
                # "categories" : Category.objects.all() JSON Error appears -> need to serialize it 
                "categories": serializer.data,
            }
        )
   
    elif request.method == "POST":
        # this is not good way to do it as there is no input validation 
        # Category.objects.create(
        #     name=request.data['name'],
        #     type=request.data['type']
        # )
        serializer = CategorySerializer(data=request.data) # serializer will validate user data input
        # print(serializer.is_valid())
        if serializer.is_valid():
            new_category = serializer.save() # serializer.save() will call create method on serializers
            return Response(
                CategorySerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)

# GET /categories/pk
# PUR /categories/pk ; update exisitng data
@api_view(["GET", "PUT", "DELETE"]) 
def categories(request,pk):
    try:
        category = Category.objects.get(pk=pk)
    except: 
        raise NotFound
    
    if request.method == "GET":
        serializer = CategorySerializer(category) 
        return(
            serializer.data
            )
    elif request.method == "PUT":
        serializer = CategorySerializer(
            category,
            data = request.data,
            partial = True, # let serializer know we only want to update part of data, not whole
        )

        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)
    elif request.method =="DELETE":
        category.delete()
        return Response(
            status=HTTP_204_NO_CONTENT
        )
        
"""