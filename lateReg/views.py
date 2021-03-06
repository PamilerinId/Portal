# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from lateReg.serializers import LateRegSerializer, LogSerializer, RegStatusSerializer
from lateReg.models import RegStatus, LateReg, Log

# Create your views here.


class RegStatusAPIView(RetrieveAPIView):
    serializer_class = RegStatusSerializer
    permission_classes = [IsAuthenticated]
    queryset = RegStatus.objects.all()


class LateRegAPIView(ListAPIView):
    serializer_class = LateRegSerializer
    permission_classes = [IsAuthenticated]
    queryset = LateReg.objects.all()


class LateRegDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LateRegSerializer
    permission_classes = [IsAuthenticated]
    queryset = LateReg.objects.all()


class LogAPIView(ListAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]
    queryset = Log.objects.all()


class LogDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LateRegSerializer
    permission_classes = [IsAuthenticated]
    queryset = LateReg.objects.all()
