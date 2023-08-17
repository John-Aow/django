import graphene
import datetime
from graphene_django import DjangoObjectType, DjangoListField 
from .models import Book, User, Order, Product, Admin, Address, Shipment, ShipmentDetail
from graphene_django.filter import DjangoFilterConnectionField

class UserType(DjangoObjectType):
    class Meta:
        model = User
        field = "__all__"

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        field = "__all__"

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        field = "__all__"

class AdminType(DjangoObjectType):
    class Meta:
        model = Admin
        field = "__all__"

class AddressType(DjangoObjectType):
    class Meta:
        model = Address
        field = "__all__"

class ShipmentType(DjangoObjectType):
    class Meta:
        model = Shipment
        field = "__all__"

class ShipmentDetailType(DjangoObjectType):
    class Meta:
        model = ShipmentDetail
        field = "__all__"


class BookType(DjangoObjectType): 
    class Meta:
        model = Book
        fields = "__all__"


class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    email = graphene.String()
    lastname = graphene.String()
    name = graphene.String()
    tel = graphene.String()


class ProductInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    price = graphene.Float()
    detail = graphene.String()

class OrderInput(graphene.InputObjectType):
    id = graphene.ID()
    product = graphene.Int()
    user = graphene.Int()
    qty = graphene.Int()
    status = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()

class AddressInput(graphene.InputObjectType):
    id = graphene.ID()
    house_no = graphene.String()
    district = graphene.String()
    sub_district = graphene.String()
    provine = graphene.String()
    street = graphene.String()
    postcode = graphene.String()

class CreateUser(graphene.Mutation):
    class Arguments:
        user_data = UserInput(required=True)
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, user_data=None):
        user_instance = User( 
            name=user_data.name,
            lastname=user_data.lastname,
            email=user_data.email,
            tel=user_data.tel
        )
        user_instance.save()
        return CreateUser(user=user_instance)

class UpdateUser():
    class Arguments:
        user_data = UserInput(require=True)
    user = graphene.Field(UserType)
    @staticmethod
    def mutate(root, info, user_data=None):

        user_instance = User.objects.get(pk=user_data.id)

        if user_instance:
            user_instance.name=user_data.name,
            user_instance.lastname=user_data.lastname,
            user_instance.email=user_data.email,
            user_instance.tel=user_data.tel

            return UpdateUser(user=user_instance)
        return UpdateUser(user=None)
    
class CreateProduct(graphene.Mutation):
    class Arguments:
        product_data = ProductInput(required=True)
    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, product_data=None):
        product_instance = Product( 
            
            name=product_data.name,
            price=product_data.price,
            detail=product_data.detail,
        )
        product_instance.save()
        return CreateProduct(product=product_instance)
    
class CreateOrder(graphene.Mutation):
    class Arguments:
        order_data = OrderInput(required=True)
    order = graphene.Field(OrderType)
    @staticmethod
    def mutate(root, info, order_data=None):
        now = datetime.datetime.now()
        order_instance = Order.objects.create( 
            qty=order_data.qty,
            user=User.objects.get(pk=order_data.user),
            product=Product.objects.get(pk=order_data.product),
            created_at=now
        )

        order_instance.save()
        return CreateOrder(order=order_instance)
    
class CreateAddress(graphene.Mutation):
    class Arguments:
        address_data = AddressInput(required=True)
    address = graphene.Field(OrderType)
    @staticmethod
    def mutate(root, info, address_data=None):
        now = datetime.datetime.now()
        address_instance = Order.objects.create( 
            house_no = address_data.house_no,
            district = address_data.district,
            sub_district = address_data.sub_district,
            provine = address_data.provine,
            street = address_data.street,
            postcode = address_data.postcode,
            user=User.objects.get(pk=address_data.user),
        )

        address_instance.save()
        return CreateAddress(address=address_instance)

class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    year_published = graphene.String()
    review = graphene.Int() 

class CreateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, book_data=None):
        book_instance = Book( 
            title=book_data.title,
            author=book_data.author,
            year_published=book_data.year_published,
            review=book_data.review
        )
        book_instance.save()
        return CreateBook(book=book_instance)
    
class UpdateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, book_data=None):

        book_instance = Book.objects.get(pk=book_data.id)

        if book_instance:
            book_instance.title = book_data.title
            book_instance.author = book_data.author
            book_instance.year_published = book_data.year_published
            book_instance.review = book_data.review
            book_instance.save()

            return UpdateBook(book=book_instance)
        return UpdateBook(book=None)
    
class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id):
        book_instance = Book.objects.get(pk=id)
        book_instance.delete()

        return None


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    
    book = graphene.Field(BookType, book_id=graphene.Int())

    all_user = graphene.List(UserType)

    all_product = graphene.List(ProductType)

    all_order = graphene.List(OrderType)

    all_address = graphene.List(AddressType)

    order = graphene.Field(OrderType, order_id=graphene.Int())

    product = graphene.Field(ProductType, product_id=graphene.Int())
    
    user = graphene.Field(UserType, user_id=graphene.Int())

    find_order = graphene.Field(OrderType, user_id=graphene.Int())


    def resolve_all_user(self, info, **kwargs):
        return User.objects.all()
    
    def resolve_all_product(self, info, **kwargs):
        return Product.objects.all()
    
    def resolve_all_order(self, info, **kwargs):
        return Order.objects.all()
   
    def resolve_product(self, info, product_id):
        return Product.objects.get(pk=product_id)
    
    def resolve_find_order(self, info, user_id):
        return Order.objects.filter(user=user_id)
    
    def resolve_order(self, info, order_id):
        return Order.objects.get(pk=order_id)

    def resolve_user(self, info, user_id):
        return User.objects.get(pk=user_id)

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_book(self, info, book_id):
        return Book.objects.get(pk=book_id)
    
class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()
    create_user = CreateUser.Field()
    create_product = CreateProduct.Field()
    create_order = CreateOrder.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)