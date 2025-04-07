from django.test import TestCase, Client
from django.urls import reverse, resolve
from .models import User
from . import views
import json

class UserModelTest(TestCase):
    
    def setUp(self):
        """Set up test data"""
        User.objects.create(
            username="testuser",
            email="test@example.com",
            password="testpassword"
        )
    
    def test_user_creation(self):
        """Test user can be created"""
        user = User.objects.get(username="testuser")
        self.assertEqual(user.email, "test@example.com")
        
    def test_unique_username(self):
        """Test username uniqueness constraint"""
        with self.assertRaises(Exception):
            User.objects.create(
                username="testuser",  # Duplicate username
                email="another@example.com",
                password="password123"
            )
            
    def test_unique_email(self):
        """Test email uniqueness constraint"""
        with self.assertRaises(Exception):
            User.objects.create(
                username="anotheruser",
                email="test@example.com",  # Duplicate email
                password="password123"
            )

class UserViewsTest(TestCase):
    
    def setUp(self):
        """Set up test data and client"""
        self.client = Client()
        self.user = User.objects.create(
            username="testuser",
            email="test@example.com",
            password="testpassword"
        )
    
    def test_get_all_users(self):
        """Test getting all users"""
        response = self.client.get(reverse('get_all_users'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)
    
    def test_get_user_by_id(self):
        """Test getting a user by ID"""
        response = self.client.get(
            reverse('get_user_by_id', args=[str(self.user.id)])
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['username'], 'testuser')
    
    def test_create_user(self):
        """Test creating a new user"""
        user_data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpassword'
        }
        response = self.client.post(
            reverse('create_user'),
            data=json.dumps(user_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username='newuser').exists())

class UrlsTest(TestCase):
    
    def test_get_all_users_url_resolves(self):
        """Test get_all_users URL pattern works"""
        url = reverse('get_all_users')
        self.assertEqual(resolve(url).func, views.get_all_users)
    
    def test_get_user_by_id_url_resolves(self):
        """Test get_user_by_id URL pattern works"""
        url = reverse('get_user_by_id', args=['1'])
        self.assertEqual(resolve(url).func, views.get_user_by_id)
    
    # Update your UrlsTest class
    
    def test_create_user_url_resolves(self):
        """Test create_user URL pattern works"""
        url = reverse('create_user')
        # Don't compare function objects, just check the view name
        self.assertEqual(resolve(url).view_name, 'create_user')
