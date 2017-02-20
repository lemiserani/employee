from django.test import TestCase, Client, LiveServerTestCase
from employees.models import Department, Employee
from django.contrib.auth.models import AnonymousUser, User
from django.utils import timezone
import json
from django.conf import settings


class DepartmentModelTestCase(TestCase):
    def setUp(self):
        Department.objects.create(name="Architecture")
        Department.objects.create(name="E-commerce")
        Department.objects.create(name="Mobile")
        Department.objects.create(name="MarketPlace")
    
    def testSize(self):
        self.assertEqual(Department.objects.all().count(), 4)
    
    def testSizeEmployee(self):
        self.assertEqual(Employee.objects.all().count(), 0)

    def test_name_label(self):
        department = Department.objects.get(name="Architecture")
        name = department._meta.get_field('name').verbose_name
        self.assertEquals(name,"name")
    
    def testDepartment(self):
        department = Department.objects.get(name="Mobile")
        self.assertEqual(department.name, "Mobile")
    
class EmployeeModelTestCase(TestCase):
    
    def setUp(self):
        self.time = timezone.now()
        self.department =  Department.objects.create(name="Finance")
        Employee.objects.create(name="Maria", email="maria@magazineluiza.com.br", department=self.department, published_date=self.time)
        Employee.objects.create(name="José", email="jose@magazineluiza.com.br", department=self.department, published_date=self.time)
        Employee.objects.create(name="João", email="joao@magazineluiza.com.br", department=self.department, published_date=self.time)
        Employee.objects.create(name="pedro", email="pedro@magazineluiza.com.br", department=self.department, published_date=self.time)
    
    def testSizeEmployee(self):
        self.assertEqual(Employee.objects.all().count(), 4)
    
    def testSizeDepartment(self):
        self.assertEqual(Department.objects.all().count(), 1)
    
    def testEmployee(self):
        employee = Employee.objects.all()[0]
        self.assertEqual(employee.name, "Maria")
        self.assertEqual(employee.email, "maria@magazineluiza.com.br")
        self.assertEqual(employee.department.name, self.department.name)
        self.assertEqual(employee.published_date, self.time)
    
    def testPublish(self):
        employee = Employee.objects.all()[0]
        self.assertTrue(employee.publish)
       
class AdminLoginTestCase(LiveServerTestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='jose', email='jose@magazineluiza', password='top_secret')

    def test_page(self):
        response = self.client.get('/admin/login/')
        self.assertEquals(response.status_code, 200)
    
    def test_login_valid(self):
        self.client.get('/admin/login/')
        self.assertEqual(True, self.client.login(username='jose', password="top_secret"))
    
    def test_login_invalid_user(self):
        self.client.get('/admin/login/')
        self.assertEqual(False, self.client.login(username='invalid', password="top_secret"))
    
    def test_login_invalid_password(self):
        self.client.get('/admin/login/')
        self.assertEqual(False, self.client.login(username='jose', password="invalid"))

class ApiDepartmentTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_without_departments(self):
        response = self.client.get('/api/v1/department/?format=json')
        self.assertEqual(response.status_code, 200)
    
    def test_with_departments(self):
        department =  Department.objects.create(name="Finance")
        department =  Department.objects.create(name="MarketPlace")
        response = self.client.get('/api/v1/department/?format=json')
        self.assertEqual(response.status_code, 200)

    def test_with_format_default(self):
        response = self.client.get('/api/v1/department/')
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_path(self):
        response = self.client.get('/api/v1/department/old')
        self.assertEqual(response.status_code, 301)
    
    def test_post_department(self):
       department = {"name": "Architecture"}
       response = self.client.post('/api/v1/department/', json.dumps(department), 'application/json')
       self.assertEqual(response.status_code, 201)
    
    def test_get_department(self):
       department =  Department.objects.create(name="MarketPlace")
       response = self.client.get('/api/v1/department/MarketPlace/')
       self.assertEqual(response.status_code, 200)
    
    def test_delete_department(self):
       department =  Department.objects.create(name="MarketPlace")
       response = self.client.delete('/api/v1/department/MarketPlace/')
       self.assertEqual(response.status_code, 204)
    
    def test_get_invalide_department(self):
        response = self.client.get('/api/v1/department/11/')
        self.assertEqual(response.status_code,404)
    
    def test_get_invalide_department(self):
        response = self.client.delete('/api/v1/department/11/')
        self.assertEqual(response.status_code,404)

class ApiEmployeeTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_without_employees(self):
        response = self.client.get('/api/v1/employee/?format=json')
        self.assertEqual(response.status_code, 200)
    
    def test_with_employees(self):
        department =  Department.objects.create(name="Finance")
        Employee.objects.create(name="Maria", email="maria@magazineluiza.com.br", department=department)
        Employee.objects.create(name="José", email="jose@magazineluiza.com.br", department=department)
        response = self.client.get('/api/v1/employee/?format=json')
        self.assertEqual(response.status_code, 200)

    def test_with_format_default(self):
        response = self.client.get('/api/v1/employee/')
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_path(self):
        response = self.client.get('/api/v1/employee/old')
        self.assertEqual(response.status_code, 301)
    
    def test_post_employee(self):
       department =  Department.objects.create(name="Architecture")
       employee = {"name":"Leandro", "email":"leandro.miserani@magazineluiza.com.br","department":{"name": "Architecture"}}
       response = self.client.post('/api/v1/employee/', json.dumps(employee), 'application/json')
       self.assertEqual(response.status_code, 201)
    
    def test_delete_404_employee(self):
        response = self.client.delete('/api/v1/employee/11/')
        self.assertEqual(response.status_code,404)
    
    def test_get_employees(self):
        department =  Department.objects.create(name="Finance")
        Employee.objects.create(id="8a40135230f21bdb0130f21c255c0007", name="José", email="jose@magazineluiza.com.br", department=department)
        response = self.client.get('/api/v1/employee/8a40135230f21bdb0130f21c255c0007/?format=json')
        self.assertEqual(response.status_code, 200)
    
    def test_delete_employees(self):
        department =  Department.objects.create(name="Finance")
        Employee.objects.create(id="8a40135230f21bdb0130f21c255c0007", name="José", email="jose@magazineluiza.com.br", department=department)
        response = self.client.delete('/api/v1/employee/8a40135230f21bdb0130f21c255c0007/?format=json')
        self.assertEqual(response.status_code, 204)
    
class SettingTestCase(TestCase):
    def test_with_specific_settings(settings):
        settings.USE_TZ = True
        assert settings.USE_TZ
    
    def test_language_using_cookie(self):
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'fr'})
        response = self.client.get('/')
        self.assertEqual(response.status_code,404)
      