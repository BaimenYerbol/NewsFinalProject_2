from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorAccount = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.authorAccount.username}'

    def update_rating(self):
        post_rat = self.post_set.aggregate(postRating=Sum('postRating'))
        prat = 0
        prat += post_rat.get('postRating')

        comment_rat = self.authorAccount.comment_set.aggregate(commentRating=Sum('commentRating'))
        crat = 0
        crat += comment_rat.get('commentRating')

        author_posts = self.post_set.all()
        pcrat = 0
        for p in author_posts:
            p_comments = p.comment_set.all()
            for c in p_comments:
                pcrat += c.commentRating

        self.authorRating = prat * 3 + crat + pcrat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    ARTICLE = 'A'
    NEWS = 'N'
    CHOICES = [
        (ARTICLE, 'Article'),
        (NEWS, 'News'),
    ]

    nameCategory = models.CharField(max_length=1, choices=CHOICES, default=NEWS)
    creationTime = models.DateTimeField(auto_now_add=True)
    head = models.CharField(max_length=128)
    text = models.TextField()
    postRating = models.IntegerField(default=0)

    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    postCategory = models.ManyToManyField(Category, through='PostCategory')

    def get_absolute_url(self):
        return f'/posts/{self.pk}'

    def like(self):
        self.postRating += 1
        self.save()

    def dislike(self):
        self.postRating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:123]}...'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentText = models.TextField()
    creationTime = models.DateTimeField(auto_now_add=True)
    commentRating = models.IntegerField(default=0)

    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentAuthor = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.commentRating += 1
        self.save()

    def dislike(self):
        self.commentRating -= 1
        self.save()
