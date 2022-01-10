from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
#  for set the limit of page 

class limit(LimitOffsetPagination,PageNumberPagination):
    pass