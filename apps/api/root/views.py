
from rest_framework import reverse, response, views, permissions, throttling
from rest_framework_api_key import permissions as APIPermissions


class APIRoot(views.APIView):
    permission_classes = [
        permissions.IsAdminUser | APIPermissions.HasAPIKey]

    throttling_classes = [throttling.UserRateThrottle,
                          throttling.AnonRateThrottle]

    def get(self, request, format=None):
        return response.Response({
            'bug-list': reverse.reverse('bug-list', request=request, format=format)
        })
