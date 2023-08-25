import graphene
import datetime
import graphql_jwt
from graphene_django import DjangoObjectType, DjangoListField 
from .models import Book, User, Order, Product, Admin, Address, Shipment, ShipmentDetail
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay, ID
from graphql_relay import from_global_id

# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         field = "__all__"

class UserTypeNode(DjangoObjectType):
    class Meta:
        model = User
        field = "__all__"
        filter_fields = {
            'id': ['exact'],
        }
        interfaces = (relay.Node,)

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        field = "__all__"
        #interfaces = (relay.Node,)

class OrderTypeNode(DjangoObjectType):
    class Meta:
        model = Order
        filter_fields = {
            'user_id': ['exact'],
            'status': ['exact', 'icontains'],
            'product': ['exact']
            # 'id': ['exact', 'icontains'],
        }
        interfaces = (relay.Node,)



class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        field = "__all__"

# class AdminType(DjangoObjectType):
#     class Meta:
#         model = Admin
#         field = "__all__"

# class AddressType(DjangoObjectType):
#     class Meta:
#         model = Address
#         field = "__all__"

# class ShipmentType(DjangoObjectType):
#     class Meta:
#         model = Shipment
#         field = "__all__"

# class ShipmentDetailType(DjangoObjectType):
#     class Meta:
#         model = ShipmentDetail
#         field = "__all__"


# class BookType(DjangoObjectType): 
#     class Meta:
#         model = Book
#         fields = "__all__"


# class UserInput(graphene.InputObjectType):
#     id = graphene.ID()
#     email = graphene.String()
#     lastname = graphene.String()
#     name = graphene.String()
#     tel = graphene.String()


# class ProductInput(graphene.InputObjectType):
#     id = graphene.ID()
#     name = graphene.String()
#     price = graphene.Float()
#     detail = graphene.String()
#     image = graphene.String()

class OrderInput(graphene.InputObjectType):
    id = graphene.ID()
    product = graphene.Int()
    user = graphene.Int()
    qty = graphene.Int()
    status = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()

# class CheckoutInput(graphene.InputObjectType):
#     list_order = graphene.List(graphene.Int)
#     user = graphene.Int()

# class AddressInput(graphene.InputObjectType):
#     id = graphene.ID()
#     house_no = graphene.String()
#     district = graphene.String()
#     sub_district = graphene.String()
#     provine = graphene.String()
#     street = graphene.String()
#     postcode = graphene.String()

# class CreateUser(graphene.Mutation):
#     class Arguments:
#         user_data = UserInput(required=True)
#     user = graphene.Field(UserType)

#     @staticmethod
#     def mutate(root, info, user_data=None):
#         user_instance = User( 
#             name=user_data.name,
#             lastname=user_data.lastname,
#             email=user_data.email,
#             tel=user_data.tel
#         )
#         user_instance.save()
#         return CreateUser(user=user_instance)

# class UpdateUser():
#     class Arguments:
#         user_data = UserInput(require=True)
#     user = graphene.Field(UserType)
#     @staticmethod
#     def mutate(root, info, user_data=None):

#         user_instance = User.objects.get(pk=user_data.id)

#         if user_instance:
#             user_instance.name=user_data.name,
#             user_instance.lastname=user_data.lastname,
#             user_instance.email=user_data.email,
#             user_instance.tel=user_data.tel

#             return UpdateUser(user=user_instance)
#         return UpdateUser(user=None)
    
# class CreateProduct(graphene.Mutation):
#     class Arguments:
#         product_data = ProductInput(required=True)
#     product = graphene.Field(ProductType)

#     @staticmethod
#     def mutate(root, info, product_data=None):
#         product_instance = Product( 
#             image=product_data.image,
#             name=product_data.name,
#             price=product_data.price,
#             detail=product_data.detail,
#         )
#         product_instance.save()
#         return CreateProduct(product=product_instance)
    
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
            created_at=now,
        )

        order_instance.save()
        return CreateOrder(order=order_instance)
    
# class Checkout(graphene.Mutation):
#     class Arguments:
#         data = CheckoutInput(required=True)
#     shipment = graphene.Field(ShipmentType)
#     @staticmethod
#     def mutate(root, info, data=None):
#         now = datetime.datetime.now()
#         shipment_instance = Shipment.objects.create(
#             created_at=now,
#             updated_at=now,
#             shipment_date=0,
#             recieved_date=0,
#             user=User.objects.get(pk=data.user),
#         )
#         shipment_instance.save()
#         #list_order
#         for x in data.list_order:
#             order = Order.objects.get(pk=x)
#             order.shipment = shipment_instance
#             order.status = 'SH'
#             order.save()
#         return Checkout(shipment=shipment_instance)

class DeleteOrder(graphene.Mutation):
    class Input:
        id = ID(required=True)

    cart_order = DjangoFilterConnectionField(OrderTypeNode)
    @staticmethod
    def mutate(root, info, **kwargs):
        model, pk = from_global_id(kwargs.get('id'))
        order_instance = Order.objects.get(id=pk)
        order_data = Order.objects.filter()
        order_instance.delete()

        return DeleteOrder(cart_order=order_data)
    
# class UpdateOrder(graphene.Mutation):
#     class Arguments:
#         order_data = OrderInput(required=True)

#     order = graphene.Field(OrderType)

#     @staticmethod
#     def mutate(root, info, order_data=None):

#         order_instance = Order.objects.get(pk=order_data.id)
#         now = datetime.datetime.now()
#         if order_instance:
#             qty=order_data.qty,
#             updated_at=now,
#             order_instance.save()

#             return UpdateBook(order=order_instance)
#         return UpdateBook(order=None)

# class CreateAddress(graphene.Mutation):
#     class Arguments:
#         address_data = AddressInput(required=True)
#     address = graphene.Field(OrderType)
#     @staticmethod
#     def mutate(root, info, address_data=None):
#         now = datetime.datetime.now()
#         address_instance = Order.objects.create( 
#             house_no = address_data.house_no,
#             district = address_data.district,
#             sub_district = address_data.sub_district,
#             provine = address_data.provine,
#             street = address_data.street,
#             postcode = address_data.postcode,
#             user=User.objects.get(pk=address_data.user),
#         )

#         address_instance.save()
#         return CreateAddress(address=address_instance)

# class BookInput(graphene.InputObjectType):
#     id = graphene.ID()
#     title = graphene.String()
#     author = graphene.String()
#     year_published = graphene.String()
#     review = graphene.Int() 

# class CreateBook(graphene.Mutation):
#     class Arguments:
#         book_data = BookInput(required=True)

#     book = graphene.Field(BookType)

#     @staticmethod
#     def mutate(root, info, book_data=None):
#         book_instance = Book( 
#             title=book_data.title,
#             author=book_data.author,
#             year_published=book_data.year_published,
#             review=book_data.review
#         )
#         book_instance.save()
#         return CreateBook(book=book_instance)
    
# class UpdateBook(graphene.Mutation):
#     class Arguments:
#         book_data = BookInput(required=True)

#     book = graphene.Field(BookType)

#     @staticmethod
#     def mutate(root, info, book_data=None):

#         book_instance = Book.objects.get(pk=book_data.id)

#         if book_instance:
#             book_instance.title = book_data.title
#             book_instance.author = book_data.author
#             book_instance.year_published = book_data.year_published
#             book_instance.review = book_data.review
#             book_instance.save()

#             return UpdateBook(book=book_instance)
#         return UpdateBook(book=None)

# class DeleteBook(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()

#     book = graphene.Field(BookType)

#     @staticmethod
#     def mutate(root, info, id):
#         book_instance = Book.objects.get(pk=id)
#         book_instance.delete()

#         return None
    
# class DeleteProduct(graphene.Mutation):
    # class Arguments:
    #     id = graphene.ID()

    # product = graphene.Field(ProductType)

    # @staticmethod
    # def mutate(root, info, id):
    #     product_instance = Product.objects.get(pk=id)
    #     product_instance.delete()

    #     return None


class Query(graphene.ObjectType):
    # all_books = graphene.List(BookType)
    
    # book = graphene.Field(BookType, book_id=graphene.Int())

    all_user = DjangoFilterConnectionField(UserTypeNode)

    all_product = graphene.List(ProductType)

    # all_order = graphene.List(OrderType)

    # all_address = graphene.List(AddressType)

    #order = DjangoFilterConnectionField(OrderTypeNode)

    # product = graphene.Field(ProductType, product_id=graphene.Int())
    
    user = relay.Node.Field(UserTypeNode)

    # find_order = graphene.List(OrderType, user_id=graphene.Int(), product_id=graphene.Int())

    cart_order = DjangoFilterConnectionField(OrderTypeNode)

    # all_ship = graphene.List(ShipmentType)


    def resolve_all_product(self, info, **kwargs):
        return Product.objects.all()
    
    # def resolve_all_order(self, info, **kwargs):
    #     return Order.objects.all()
   
    # def resolve_product(self, info, product_id):
    #     return Product.objects.get(pk=product_id)
    
    # def resolve_cart_order(self, info, **kwargs):
    #     print(kwargs)
    #     return Order.objects.filter()
    
    # def resolve_find_order(self, info, user_id, product_id):
    #     return Order.objects.filter(user__id=user_id, product__id=product_id, status='CA')
    
    # def resolve_order(self, info, order_id):
    #     return Order.objects.get(pk=order_id)

    # def resolve_user(self, info, user_id):
    #     return User.objects.get(pk=user_id)

    # def resolve_all_books(self, info, **kwargs):
    #     return Book.objects.all()

    # def resolve_book(self, info, book_id):
    #     return Book.objects.get(pk=book_id)
    
    # def resolve_all_shipment():
    #     return Shipment.objects.all()
    
class Mutation(graphene.ObjectType):
#    pass
#     token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()
#     create_book = CreateBook.Field()
#     update_book = UpdateBook.Field()
#     delete_book = DeleteBook.Field()
#     create_user = CreateUser.Field()
#     create_product = CreateProduct.Field()
    create_order = CreateOrder.Field()
#     delete_product = DeleteProduct.Field()
    delete_order = DeleteOrder.Field()
#     checkout = Checkout.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)