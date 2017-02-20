from django.conf.urls import url, include
from django.contrib import admin
from employees.api import EmployeeResource, DepartmentResource
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(EmployeeResource())
v1_api.register(DepartmentResource())

urlpatterns = [ url(r'^api/', include(v1_api.urls)),
                url(r'^admin/', admin.site.urls),
                url(r'^healthcheck/', include('health_check.urls'))
                ]