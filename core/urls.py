from django.urls import  path


from .views import *
urlpatterns = [
    path('',HomeApi.as_view()),
    path('programming-languages/',ProgrammingLanguagesAPI.as_view(),name='programming_languages'),
    path('footer-data/',FooterDataAPI.as_view(),name='footer_data'),
    path('contacts/',ContactUsAPI.as_view()),

    #portfolio
    path('portfolio/all/', PortfolioAPI.as_view(), name='portfolio_list'),
    
    path('portfolio/categories/',PortfolioCategoriesAPI.as_view(),name='portfolio_category'),
    path('portfolio/category/<str:slug>/',PortfolioCategoryDetailAPI.as_view(),name='portfolio_category_detail'),
    path('portfolio/<str:slug>/', PortfolioDetailAPI.as_view(), name='portfolio_list'),

    #services

    path('service-categories/',ServicesCategoryAPI.as_view(),name='service_category_list'),
    path('service-categories/<str:slug>/',ServicesCategoryDetailAPI.as_view(),name='service_category'),
    path('services/',ServicesAPI.as_view(),name='services_list'),
    path('services/<str:slug>/',ServicesDetailAPI.as_view(),name='service'),
    #abouts
    path('about-us/', AboutUsAPI.as_view({'get':'list'})),
    path('partners/', PartnersAPIView.as_view()),
    #teachers
    path('teachers/', TeachersAPI.as_view({'get':'list'})),
    path('profile/me/', ProfileAPI.as_view({'get':'list'})),
    path('blog-categories/',BlogCategoryAPI.as_view({'get':'list'})),
    path('blog/',BlogAPI.as_view({'get':'list'})),
    path('blog/<str:slug>/',BlogDetailsViewSet.as_view(),name='blog_det'),
    # path('tag/<str:slug>/',TagsSerializerAPI.as_view()),
    path('vacancies/',VacanciesListView.as_view(),name='vacancies'),
    path('texts/',TextContextAPI.as_view(),name='texts'),
    
    path('vacancies/<str:slug>/',VacanciesRetreeView.as_view(),name='vacancy'),
    path('vacancies/<str:slug>/subs/',VacansySubscribeView.as_view(),name='vacansy_subs')


]

