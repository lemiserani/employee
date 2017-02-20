from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from employees.models import Employee, Department
from django.utils import timezone
from tastypie import fields

class DepartmentResource(ModelResource):
    name = fields.CharField(attribute='name')
    class Meta:
        queryset = Department.objects.all()
        filtering = {'name': ALL}
        authorization = Authorization()
        excludes = ['id']
        allowed_methods = ['get', 'post', 'delete']

class EmployeeResource(ModelResource):
    department = fields.ForeignKey(DepartmentResource, 'department', full=True)
    
    class Meta:
        queryset = Employee.objects.all()
        include_resource_uri = False
        include_absolute_url = False
        authorization = Authorization()
        excludes = ['created_date', 'id', 'published_date']
        allowed_methods = ['get', 'post', 'delete']
    
    def dehydrate(self, bundle):
         bundle.data['department'] = bundle.data.get('department').data.get("name")
         return bundle