from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Citizen, Mayor
from users.serializers import DetailCitizenSerializer, AllCitizenSerializer, AllMayorSerializer, DetailMayorSerializer


class Citizens_list(APIView):
    """
    List of all citizens or create new citizen
    :param request:
    :return:
    """
    def get(self, request, format=None):
        citizens = Citizen.objects.filter()
        serializer = AllCitizenSerializer(citizens, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DetailCitizenSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Citizens_detail(APIView):
    """
    Get, Update or Delete a citizen
    :param request:
    :param pk: Primary Key of the citizen
    :return:
    """

    def get_object(self, pk):
        try:
            return Citizen.objects.get(pk=pk)
        except Citizen.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        citizen = self.get_object(pk)
        serializer = DetailCitizenSerializer(citizen)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        citizen = self.get_object(pk)
        serializer = DetailCitizenSerializer(citizen, data=request.DATA)
        if serializer.is_valid():
            s = serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        citizen = self.get_object(pk)
        citizen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Mayor_list(APIView):
    """
    List of mayor or create a new citizen
    """

    def get(self, request, format=None):
        mayors = Mayor.objects.filter()
        serializer = AllMayorSerializer(mayors, many=True)
        return Response(serializer.data)


class Mayor_detail(APIView):

    def get_object(self, pk):
        try:
            return Mayor.objects.get(pk=pk)
        except Mayor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        mayor = self.get_object(pk)
        serializer = DetailMayorSerializer(mayor)
        return Response(serializer.data)