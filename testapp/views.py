from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Check if regid is provided in the request
            regid = request.query_params.get('regid', None)

            if regid:
                # Single employee request
                employee = Employee.objects.get(regid=regid)
                if employee:
                    # Format success response for single employee request
                    serializer = EmployeeSerializer(employee)
                    return Response({"message": "Employee details found", "success": True, "employees": [serializer.data]}, status=status.HTTP_200_OK)
                else:
                    # Employee not found with the provided regid
                    return Response({"message": f"No employee found with regid {regid}", "success": False, "employees": []}, status=status.HTTP_200_OK)
            else:
                # All employee request
                employees = Employee.objects.all()
                serializer = EmployeeSerializer(employees, many=True)
                return Response({"message": "Employee details found", "success": True, "employees": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": "Error retrieving employee details", "success": False, "employees": []}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            # Check for duplicate employee registration by email
            email = request.data.get('email')
            if Employee.objects.filter(email=email).exists():
                return Response({"message": "Employee already exists", "success": False}, status=status.HTTP_409_CONFLICT)

            # Continue with employee creation
            serializer = EmployeeSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                regid = serializer.data.get('regid', None)
                return Response({"message": "Employee created successfully", "regid": regid, "success": True}, status=status.HTTP_200_OK)
            else:
                # Check for missing required fields or invalid data types
                if 'name' in serializer.errors or 'email' in serializer.errors or 'age' in serializer.errors:
                    return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"message": "Employee creation failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            print(e)
            return Response({"message": "Employee creation failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
    def put(self, request, pk, *args, **kwargs):
        try:
            # Check if the employee exists with the provided regid
            employee = Employee.objects.get(pk=pk)
            
            if not employee:
                return Response({"message": f"No employee found with regid {pk}", "success": False}, status=status.HTTP_200_OK)

            # Validate data types and required keys
            self.validate_data_types(request.data)

            # Continue with employee update
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            # Format success response
            return Response({"message": "Employee details updated successfully", "success": True}, status=status.HTTP_200_OK)

        except ValueError as e:
            return Response({"message": str(e), "success": False}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": "Employee updation failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, pk, *args, **kwargs):
        try:
            # Check if the employee exists with the provided regid
            employee = Employee.objects.get(pk=pk)
            if employee is None:
                return Response({"message": f"No employee found with regid {pk}", "success": False}, status=status.HTTP_200_OK)

            # Continue with employee deletion
            employee.delete()

            # Format success response
            return Response({"message": "Employee deleted successfully", "success": True}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": "Employee deletion failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def validate_data_types(self, data):
        # Implement data type validation logic here
        pass

    def validate_required_keys(self, data):
        # Implement required keys validation logic here
        pass
