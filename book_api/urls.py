from django.urls import path
# from book_api.views import book_list, book_create, book
from book_api.views import BookList, BookCreate, BookDetail

urlpatterns = [
    # -------- URL FOR FUNCTION BASE VIEWS (REST API) --------
    # path('', book_create),
    # path('list/', book_list),
    # path('<int:pk>', book)
    
    # -------- URL FOR CLASS BASE VIEWS (REST API) --------
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    path('<int:pk>', BookDetail.as_view())
    
]
