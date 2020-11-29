import graphene
from graphene_django import DjangoConnectionField, DjangoListField, DjangoObjectType
from .models import Quizzes, Question, Answer, Category




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



# query part starts with the Types defined
class Query(graphene.ObjectType):
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        

        # have to use get hete cause it only returns one item cause its made with graphene.Field
        return Question.objects.get(id=id)
    
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question__id=id)



#// exporting the graphene schema
schema = graphene.Schema(query=Query)