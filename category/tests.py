from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from django.contrib.auth import get_user_model
from .models import Category
from .views import CategoryViewSet

User = get_user_model()


class CategoryTest(APITestCase):
    def setUp(self, *args, **kwargs):
        self.factory = APIRequestFactory()
        self.setup_category()
        self.user = self.setup_user()

    def setup_user(self):
        return User.objects.create_superuser('test@gmail.com', '1')

    def setup_category(self):
        # Category.objects.create(name='category_1')
        # Category.objects.create(name='category_2')
        # Category.objects.create(name='category_3')
        list_categories = []
        for i in range(1,101):
            list_categories.append(Category(name=f'category{i}', slug=f'slug{i}'))
        Category.objects.bulk_create(list_categories)

    def test_get_category(self):
        request = self.factory.get('api/categories/')
        view = CategoryViewSet.as_view({'get': 'list'})
        response = view(request)

        assert response.status_code == 200
        assert Category.objects.count() == 100
        assert Category.objects.first().name == 'category1'

    def test_post_category(self):
        data = {
            'name': 'test_category'
        }
        request = self.factory.post('api/categories/', data)
        force_authenticate(request, user=self.user)
        view = CategoryViewSet.as_view({'post': 'create'})
        response = view(request)

        assert response.status_code == 201
        assert Category.objects.filter(name='test_category').exists()
