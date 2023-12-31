from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("name","email","password")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def save(self):
        user = get_user_model()(
            email=self.validated_data ["email"],
            name=self.validated_data["name"]
        )

        password = self.validated_data["password"]

        user.set_password(password)
        user.save()

        return user
