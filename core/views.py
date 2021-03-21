from rest_framework import permissions
from rest_framework.generics import \
    ListAPIView,\
    CreateAPIView,\
    RetrieveAPIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .utils import SendEmailContacts
from .serializers import *
from .models import *


class HomeApi(ListAPIView):
    
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer



class TextContextAPI(ListAPIView):

    queryset = TextContext.objects.all()
    serializer_class = TextContextSerializer


class ProgrammingLanguagesAPI(ListAPIView):

    queryset = ProgrammingLanguages.objects.all()
    serializer_class = ProgrammingLanguagesSerializer

class FooterDataAPI(ListAPIView):

    queryset = FooterData.objects.all()
    serializer_class = FooterDataSerializer


class ContactUsAPI(CreateAPIView):

    serializer_class = CreateContactUsSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        SendEmailContacts.send_email(request.data)
        

        return Response(status=200)


class PortfolioCategoriesAPI(ListAPIView):

    queryset = PortfolioCategory.objects.all()
    serializer_class = PortfolioCategorySerializer

class PartnersAPIView(ListAPIView):

    queryset = Partners.objects.all()
    serializer_class = PartnerSerializer

class PortfolioAPI(ListAPIView):

    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioCategoryDetailAPI(RetrieveAPIView):

    queryset = PortfolioCategory.objects.all()
    serializer_class = PortfolioCategorySerializer
    lookup_field = 'slug'


class PortfolioDetailAPI(RetrieveAPIView):

    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    lookup_field = 'slug'

class ServicesCategoryAPI(ListAPIView):

    queryset = ServiceCategory.objects.all()
    serializer_class = ServicesCategorySerializer
#

class ServicesCategoryDetailAPI(RetrieveAPIView):

    queryset = ServiceCategory.objects.all()
    serializer_class = ServicesCategorySerializer
    lookup_field = 'slug'


class ServicesAPI(ListAPIView):

    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
    
    
class ServicesDetailAPI(RetrieveAPIView):

    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
    lookup_field = 'slug'

class AboutUsAPI(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class =  AboutUsSerializer

class TeachersAPI(ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

class ProfileAPI(ModelViewSet):

    # queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

class BlogCategoryAPI(ModelViewSet):

    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class BlogAPI(ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailsViewSet(RetrieveAPIView):
    
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'slug'
    
    def get(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog,slug=kwargs['slug'])
        if not kwargs['slug']  in request.session:
            blog.views_count += 1
            blog.save()
            self.request.session[kwargs['slug']] = kwargs['slug']
        return self.retrieve(request, *args, **kwargs)



class TagsSerializerAPI(RetrieveAPIView):

    queryset = Tag.objects.all()
    lookup_field = 'slug'
    serializer_class = PostSerializer

    

class VacanciesListView(ListAPIView):

    queryset = Vacancies.objects.all()
    serializer_class = VacancySerializer


class VacanciesRetreeView(RetrieveAPIView):

    queryset = Vacancies.objects.all()
    serializer_class = VacancySerializer
    lookup_field = 'slug'


class VacansySubscribeView(CreateAPIView):

    serializer_class = SubsVacanySerializer

    def post(self,request,*args,**kwargs):
        serializer = SubsVacanySerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save(vacancy_id=Vacancies.objects.get(slug__iexact=kwargs['slug']).id)
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)
        

