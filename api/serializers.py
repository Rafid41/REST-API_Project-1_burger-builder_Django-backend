# api\serializers.py
# serialize means convert model to json
from rest_framework import serializers
from .models import User, Order, Ingredient, CustomerDetail


class UserSerializer(serializers.ModelSerializer):
    # pass read kora jabena
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={
            "input_type": "password",
        },
    )

    class Meta:
        model = User
        fields = ["id", "email", "password"]

    # overwrite built-in create fn of ModelSerializer
    # validated data er moddhe email, pass etc thake
    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        # User Model er create_user fn
        user = User.objects.create_user(email, password)
        return user


################### Serialize Order ##################


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    # foreignKey thakle shei model er Field k vinno vabe serialize korte hbe
    ingredients = IngredientSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = "__all__"

    # nested serializer silo, tai by default create hbe na
    # manually create() call kore overwrite korte hbe
    def create(self, validated_data):

        ingredient = validated_data["ingredients"]
        customer = validated_data["customer"]
        price = validated_data["price"]
        orderTime = validated_data["orderTime"]
        user = validated_data["user"]

        # print(ingredient)

        # create /update Order model
        order = Order.objects.create(
            ingredients=IngredientSerializer.create(IngredientSerializer(), ingredient),
            customer=CustomerSerializer.create(CustomerSerializer(), customer),
            orderTime=orderTime,
            price=price,
            user=user,
        )


        return order
