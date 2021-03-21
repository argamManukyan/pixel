from rest_framework import serializers

from .models import *


class HomePageSerializer(serializers.ModelSerializer):

    class  Meta:
        model = HomePage
        fields = "__all__"
        
        
class ProgrammingLanguagesSerializer(serializers.ModelSerializer):

    class  Meta:
        model = ProgrammingLanguages
        fields = "__all__"
        




class FooterIconSerializer(serializers.ModelSerializer):

    class  Meta:
        model = FooterIcon
        fields = "__all__"
        
        
class FooterDataSerializer(serializers.ModelSerializer):
    
    footericon = FooterIconSerializer(many=True)
    class  Meta:
        model = FooterData
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):

    class  Meta:
        model = Partners
        fields = "__all__"

class CreateContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = ['name','email','phone','message']

   

class PortfolioImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioVideoUploads
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):

    images_portfolio = PortfolioImageSerializer(many=True)
    service = serializers.SlugRelatedField(slug_field='name',read_only=True)
    class Meta:
        model = Portfolio
        fields = "__all__"


class PortfolioCategorySerializer(serializers.ModelSerializer):

    portfolio = PortfolioSerializer(many=True)
    class Meta:
        model = PortfolioCategory
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field='username',read_only=True)

    class Meta:

        model = Profile
        fields = "__all__"


#
class ServicesItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceItem
        fields = "__all__"
#
class ServicesSerializer(serializers.ModelSerializer):

    service_item = ServicesItemSerializer(many=True)
    category = serializers.SlugRelatedField(slug_field='name',read_only=True)

    class Meta:
        model = Service
        fields = "__all__"



class ServicesCategorySerializer(serializers.ModelSerializer):


    service = ServicesSerializer(many=True)
    class Meta:
        model = ServiceCategory
        fields = "__all__"

    def get_service(self,obj):
        return obj.sevice.name


class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teachers
        fields = "__all__"

class TextContextSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextContext
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):


    class Meta:

        model = Tag
        fields = "__all__"


class BlogCategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = BlogCategory
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(read_only=True)

    class Meta:
        model=User
        fields = ['username','profile']

class BlogSerializer(serializers.ModelSerializer):


    category = BlogCategorySerializer()
    author = UserSerializer()
    tag = TagSerializer(many=True)
    class Meta:
        model = Blog
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    blog_posts = BlogSerializer(many=True)

    class Meta:
        model = Tag
        fields = "__all__"


"""VACANCIES"""

class VacancyTeamImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacancyTeamImages
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):

    images = VacancyTeamImagesSerializer(many=True)
    
    class Meta:
        model = Vacancies
        fields = "__all__"


class SubsVacanySerializer(serializers.ModelSerializer):

    class Meta:
        model = VacancySubscribe
        exclude = ['vacancy']
