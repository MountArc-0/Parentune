from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# class LoginSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = User
#         fields = ('email', 'password')
#
#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')
#
#         if not User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({"email": "Email not found."})
#
#         user = User.objects.get(email=email)
#
#         if not user.check_password(password):
#             raise serializers.ValidationError({"password": "Incorrect password."})
#
#         return attrs

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = self.user.username
        return data
