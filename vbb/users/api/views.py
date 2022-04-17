from django.contrib.auth import authenticate, get_user_model, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    action,
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from vbb.users.api.serializers import UserSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


# TODO : Add Authorisation Here
# TODO : Move to Class Based Views
@api_view(["GET"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def example_protected_route(request: Request) -> Response:
    serializer = UserSerializer(
        User.objects.all(), context={"request": request}, many=True
    )
    return Response(status=status.HTTP_200_OK, data=serializer.data)


@api_view(["POST"])
@csrf_exempt
@permission_classes([])
def login_user(request: Request) -> Response:
    body = request.data.get("data")
    username = body.get("username")
    password = body.get("password")
    email = request.data.get("email")
    user = None

    # authenticate the user either through username or email
    if username:
        user = authenticate(username=username, password=password)
    elif email:
        user = authenticate(username=email, password=password)
    else:
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={"message": "You must supply a username or email"},
        )
    if user is None:
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={"message": "Incorrect login information"},
        )

    serialized_user = UserSerializer(
        user,
        context={"request": request},
    )
    login(request, user, backend=user.backend)
    response = Response(data={"user": serialized_user.data})
    return response
