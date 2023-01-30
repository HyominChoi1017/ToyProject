from django.db import models

# Create your models here.


# User
def get_default_User_favDate():
    return {"artist":[],"album":[],"music":[]}
def get_default_User_relationShip():
    return {"follower":[],"following":[]}
def get_default_User_interestedPost():
    return {"likedPost":[],"savedPost":[]}
class User(models.Model): # 
    id = models.IntegerField(default=1, primary_key=True)
    Username = models.CharField(default="User", max_length=20) #Username를 email부분으로 하겠습니다. / 이메일부분 중복 안되게 했습니다.
    Name = models.CharField(default="noname", max_length=20)
    Password = models.CharField(default="", max_length=20)

    ProfileImg = models.ImageField(upload_to="ProfileImg", blank=True)  # 사용자가 직접 업로드하는 이미지이기 때문에 media폴더 안에 들어가야 한다. <- 만약 그렇게 않을 경우 수정 필요.

    favData = models.JSONField(default=get_default_User_favDate) # 즐겨찾는 아티스트, 앨범, 음악을 저장함. 배열 속에 저장되는 데이터는 각 데이터의 식별자를 암호화한 내용임. (지정된 길이의 문자열로 암호화)

    relationShip = models.JSONField(default=get_default_User_relationShip)

    intrestedPost = models.JSONField(default=get_default_User_interestedPost)
    class Mete:
        db_table='users'
    
    def __str__(self):
        return "[{}] {}".format(self.id, self.Username)


def get_default_Play_Date():
    return {'artist':"", 'music':""}
class Playlist(models.Model):
    user_id = models.ForeignKey("User", related_name="playlist_user", on_delete=models.CASCADE, db_column="playlist_user_id", default=1)
    Title = models.CharField(default="My PlayList", max_length=20)
    Data = models.JSONField(default=get_default_Play_Date)


def get_default_Post_Tag():
    return {"location":"","user":[]}
class Post(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    user_id = models.ForeignKey("User", related_name="post_user", on_delete=models.CASCADE, db_column="post_user_id", default=1)

    AlbumCover = models.URLField()
    MusicData = models.URLField() # 외부 rest api로 불러오기 때문에
    Content = models.CharField(default="", max_length=300)
    
    Like = models.IntegerField(default=0)
    Tag = models.JSONField (default=get_default_Post_Tag)

    def __str__(self):
        return "{} : {}".format(self.user_id, self.Content)

class Comment(models.Model):
    post_id = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE, db_column="post_id")

    id = models.BigAutoField(help_text="Comment ID", primary_key=True)
    userid = models.IntegerField(default=1)
    contents = models.TextField(help_text="Comment contents", blank=False, null=False)
    like = models.IntegerField(default=0)

    def __str__(self):
        return "{}:{}".format(self.userid, self.contents)
    