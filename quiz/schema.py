import graphene
from graphene_django import DjangoConnectionField, DjangoListField, DjangoObjectType
from .models import Quizzes, Question, Answer, Category



##################   WHAT IS RETURNED SECTION #######################################
# converts models into graphs
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id","title","category")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question","answer_text")

################## WHAT IS RETURNED SECTION ENDS HERE ##############################






# Mutation part

class CategoryAddMutation(graphene.Mutation):

    # this is just what gets returned, after crud if present
    category = graphene.Field(CategoryType)


    # argument passed, in this case it accepts name
    class Arguments:
        name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryAddMutation(category=category)



class CategoryUpdateMutation(graphene.Mutation):

    # this is just what gets returned, after crud if present
    category = graphene.Field(CategoryType)


    # argument passed, in this case it accepts name
    class Arguments:
        name = graphene.String(required=True)
        id   = graphene.Int(required=True)

    @classmethod
    def mutate(cls, root, info, id, name):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return CategoryUpdateMutation(category=category)



class CategoryDeleteMutation(graphene.Mutation):

    # this is just what gets returned, after crud if present
    category = graphene.Field(CategoryType)


    # argument passed, in this case it accepts name
    class Arguments:
        id   = graphene.Int(required=True)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()

        # in case of delete null is returned
        return None




# this is just a place to link all the mutationfields
# no function adding is done here
class Mutation(graphene.ObjectType):


    # this is converted to mutation function in the frontend as updateCategory
    createCategory = CategoryAddMutation.Field()
    updateCategory = CategoryUpdateMutation.Field()
    deleteCategory = CategoryDeleteMutation.Field()







# query part

# query part starts with the Types defined
class Query(graphene.ObjectType):
    
    # front end query fields
    allQuestions = graphene.Field(QuestionType, id=graphene.Int())
    allAnswers = graphene.List(AnswerType, id=graphene.Int())

    
    
    def resolve_alQuestions(root, info, id):
        

        # have to use get hete cause it only returns one item cause its made with graphene.Field
        return Question.objects.get(id=id)
    
    def resolve_allAnswers(root, info, id):
        return Answer.objects.filter(question__id=id)




#// exporting the graphene schema
schema = graphene.Schema(query=Query, mutation=Mutation)