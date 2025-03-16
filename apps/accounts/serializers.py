from rest_framework import serializers

from .models import User


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    # role = serializers.ChoiceField(
    #     choices=User.ROLE_CHOICES, required=False, default=User.ROLE_USER
    # )

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
            "tags",
            "created_at",
            "updated_at",
            "is_business",
            "is_active",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")  # Remove a senha dos dados validados
        user = User(**validated_data)  # O role já está em validated_data corretamente
        user.set_password(password)  # Criptografa a senha
        user.save()
        return user
