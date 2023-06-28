from api.v1.filters import EventFilterSet
from api.v1.paginators import PageLimitPagination
from api.v1.permissions import IsAdminAuthorOrReadOnly
from api.v1.serializers import (CitySerializer, EventReadSerializer,
                                EventWriteSerializer, TagSerializer,
                                TopicSerializer)
from api.v1.utils import search_events
from django.db.models import Count
from django.http import FileResponse
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from events.models import City, Event, Favourite, Tags, Topic
from rest_framework import exceptions, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class EventsViewSet(ModelViewSet):
    permission_classes = (IsAdminAuthorOrReadOnly,)
    pagination_class = PageLimitPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilterSet
    http_method_names = ['get', 'patch', 'delete', 'post']

    def get_queryset(self):
        query = self.request.query_params.get('search', '')
        return Event.objects.all() if not query else search_events(query)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return EventReadSerializer
        return EventWriteSerializer

    def perform_create(self, serializer):
        if not self.request.user.is_manager:
            raise exceptions.PermissionDenied("У вас нет прав.")

        organization = self.request.user.organization

        event_data = serializer.validated_data
        event_data['organizer'] = organization

        serializer.save()

    @action(detail=False, methods=["get"])
    def popular(self, request):
        """Маршрутизатор для вывода списка популярных событий"""
        events = Event.objects.filter(date_start__gte=timezone.now())
        popular_tags = events.values('tags').annotate(
            tag_count=Count('tags')).order_by('-tag_count')
        sorted_tag_ids = [
            tag['tags'] for tag in popular_tags
        ]
        queryset = Event.objects.filter(
            tags__in=sorted_tag_ids).order_by('-date_start')
        page = self.paginate_queryset(queryset)
        serializer = EventReadSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=False, methods=["get"],
            permission_classes=[IsAuthenticated])
    def favorites(self, request: Request):
        """Маршрутизатор для вывода списка ивентов
        находящихся в Избранном пользователя"""
        queryset = Event.objects.filter(favourite__user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = EventReadSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = EventReadSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"],
            permission_classes=[IsAuthenticated])
    def toggle_favorite(self, request: Request, pk: int):
        """Маршрутизатор для добавления и удаления ивентов
        из Избранного пользователя"""
        event = self.get_object()
        favorite = Favourite.objects.filter(user=request.user,
                                            event=event).first()

        if favorite:
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        Favourite.objects.create(user=request.user, event=event)
        return Response(status=status.HTTP_201_CREATED)


class TagsViewSet(ModelViewSet):
    serializer_class = TagSerializer
    http_method_names = ['get']
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = Tags.objects.annotate(event_count=Count('event'))
        return queryset.order_by('-event_count')


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    http_method_names = ['get']
    filter_backends = [SearchFilter]
    search_fields = ['name']


class TopicsViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    http_method_names = ['get']
    filter_backends = [SearchFilter]
    search_fields = ['name']


def cookies_view(request):
    file_path = "cookies.pdf"
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')


def privacy_view(request):
    file_path = "privacy.pdf"
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
