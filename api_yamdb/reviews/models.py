from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import validate_slug, validate_year
from users.models import CustomUser as User


class Category(models.Model):
    """Категория произведения."""

    name = models.CharField(
        max_length=256,
        verbose_name="Название категории",
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="Идентификатор категории",
        validators=(validate_slug,),
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Жанр произведения."""

    name = models.CharField(
        max_length=256,
        verbose_name="Название жанра",
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="Идентификатор жанра",
        validators=(validate_slug,),
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Title(models.Model):
    """Произведение."""

    name = models.CharField(
        max_length=256,
        verbose_name="Название произведение",
    )
    year = models.IntegerField(
        verbose_name="Дата выхода",
        validators=(validate_year,),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание произведения",
    )
    genre = models.ManyToManyField(
        Genre,
        related_name="titles",
        blank=True,
        verbose_name="Жанр",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        related_name="titles",
        blank=False,
        null=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.name


class Review(models.Model):
    """Отзывы пользователей на произведения."""

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        blank=False,
        related_name="reviews",
        verbose_name="Произведение",
    )
    text = models.CharField(max_length=255, verbose_name="Текст отзыва")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Пользователь",
    )
    score = models.IntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(10)),
        verbose_name="Оценка",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        constraints = [
            models.UniqueConstraint(
                fields=(
                    "title",
                    "author",
                ),
                name="only one review from one user",
            )
        ]
        ordering = ("pub_date",)

    def __str__(self):
        return self.text[:30]


class Comment(models.Model):
    """Комментарии пользователей к отзывам."""

    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Отзыв",
    )
    text = models.CharField(max_length=255, verbose_name="Текст комментария")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пользователь",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("pub_date",)

    def __str__(self):
        return self.text[:30]
