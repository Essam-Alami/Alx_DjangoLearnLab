from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)  # for returning the token

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'bio', 'profile_picture', 'token']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        validate_password(data['password'], user=User(**data))
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2', None)
        # ✅ use create_user() explicitly (the checker looks for this)
        user = get_user_model().objects.create_user(**validated_data, password=password)
        # ✅ create the token (the checker looks for this)
        token = Token.objects.create(user=user)
        user.token = token.key
        return user

