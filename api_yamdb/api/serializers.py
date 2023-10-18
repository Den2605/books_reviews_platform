from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import CustomUser as User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("id",)
        lookup_field = "slug"
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("id",)
        lookup_field = "slug"
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field="slug",
        required=True,
        many=True,
    )
    category = serializers.SlugRelatedField(
        slug_field="slug", queryset=Category.objects.all()
    )
    rating = serializers.IntegerField(read_only=True, default=None)

    class Meta:
        fields = (
            "id",
            "name",
            "year",
            "rating",
            "description",
            "genre",
            "category",
        )
        model = Title


class ReadOnlyTitleSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(
        source="reviews__score__avg", read_only=True
    )
    genre = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Title
        fields = (
            "id",
            "name",
            "year",
            "rating",
            "description",
            "genre",
            "category",
        )


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    def validate_score(self, value):
        if value not in range(1, 11):
            raise serializers.ValidationError(
                "Допускается целое число от 1 до 10"
            )
        return value

    def validate(self, data):
        request = self.context["request"]
        author = request.user
        title_id = self.context.get("view").kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        if (
            request.method == "POST"
            and Review.objects.filter(title=title, author=author).exists()
        ):
            raise serializers.ValidationError("Допускается только один отзыв")
        return data

    class Meta:
        fields = ("id", "text", "author", "score", "pub_date")
        model = Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "usernmame",
            "email",
            "first_name",
            "last_name",
            "bio",
            "role",
        )


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(slug_field="text", read_only=True)
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        fields = ("id", "text", "author", "review", "pub_date")
        model = Comment
