from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialiizers import StudentSerializer
from .models import Student
from rest_framework import status

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def studentapi(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                stu = Student.objects.get(id=id)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
            data = StudentSerializer(stu,many=True).data
            return Response(data)
        stu = Student.objects.all()
        data = StudentSerializer(stu, many=True).data
        return Response(data)
    elif request.method == 'POST':
        serializer  =StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':f'Data Inserted Successfull','Data':f'{request.data}'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        id = request.data.get('id')
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(stu ,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':f'Data Updated Successfull','Data':f'{request.data}'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
            id = request.data.get('id')
            try:
                stu = Student.objects.get(id=id)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Msg': 'Data Updated Successfully via PATCH', 'Data': serializer.data}, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        id = request.query_params.get('id')
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        stu.delete()
        return Response({'Msg':f'Data Deleted Successfull','Data':f'{request.data}'},status=status.HTTP_202_ACCEPTED)