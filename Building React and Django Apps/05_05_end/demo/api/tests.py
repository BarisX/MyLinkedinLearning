from datetime import timedelta
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.core.cache import cache
from django.utils import timezone
import oauth2_provider.models
from api.models import Package, PackagePermission
from api.serializers import BookingSerializer

Application = oauth2_provider.models.get_application_model()
AccessToken = oauth2_provider.models.get_access_token_model()

def create_access_token(user):
    token_expiration_time = timezone.now() + timedelta(minutes=60)
    token = AccessToken.objects.create(
        user=user,
        scope='read write packages',
        token='test{}{}'.format(
            user.id,
            int(token_expiration_time.timestamp()),
        ),
        application=Application.objects.first(),
        expires=token_expiration_time,
    )
    return token

def auth_header(token):
    return { 'HTTP_AUTHORIZATION': 'Bearer {}'.format(token) }

class CachingTestCase(APITestCase):
    def test_wishlist_cache(self):
        package = Package.objects.create(category='a', name='package', price=0.0, rating='medium', tour_length=1)
        self.assertIsNone(cache.get('wishlist:wishlist-items'))
        response = self.client.get('/api/v1/wishlist/')
        self.assertListEqual(response.data, [])
        self.assertListEqual(cache.get('wishlist:wishlist-items'), [])

        response = self.client.post('/api/v1/wishlist/', { 'id': package.id })
        self.assertIsNone(cache.get('wishlist:wishlist-items'))

        response = self.client.get('/api/v1/wishlist/')
        self.assertListEqual(response.data, [package.id])
        self.assertListEqual(cache.get('wishlist:wishlist-items'), [package.id])
