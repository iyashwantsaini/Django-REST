from django.urls import path,include
# from .views import article_list,article_detail
from .views import ArticleAPIView,ArticleAPIDetailsView
from .views import GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'article', ArticleViewSet,basename='article')
# urlpatterns = router.urls

urlpatterns = [
    # fn based
    # path('article/',article_list),
    # path('article/<int:pk>/',article_detail),
    # class based
    path('article/',ArticleAPIView.as_view()),
    path('article/<int:id>/',ArticleAPIDetailsView.as_view()),
    # generic
    path('generic/', GenericAPIView.as_view()),
    path('generic/<int:id>/', GenericAPIView.as_view()),

    # view sets
    # as basename=article => access by url => viewset/article
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
]
