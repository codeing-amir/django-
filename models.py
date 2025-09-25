from django.db import models
from django.contrib.auth.models import User

class PersonalInfo(models.Model):
    # ❌ خطا: objects = None  رو حذف کن
    DoesNotExist = None
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="نام کامل")
    title = models.CharField(max_length=200, verbose_name="عنوان شغلی")
    initials = models.CharField(max_length=10, verbose_name="حروف اول")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=15, verbose_name="شماره تماس")
    location = models.CharField(max_length=100, verbose_name="موقعیت")
    bio = models.TextField(verbose_name="بیوگرافی")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    class Meta:
        verbose_name = "اطلاعات شخصی"
        verbose_name_plural = "اطلاعات شخصی"

    def __str__(self):
        return self.name

class Education(models.Model):
    # ❌ خطا: objects = None  رو حذف کن
    objects = None
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100, verbose_name="مدرک")
    university = models.CharField(max_length=100, verbose_name="دانشگاه")
    field = models.CharField(max_length=100, verbose_name="گرایش")
    description = models.TextField(verbose_name="توضیحات")
    start_date = models.DateField(verbose_name="تاریخ شروع")
    end_date = models.DateField(verbose_name="تاریخ پایان", null=True, blank=True)
    is_current = models.BooleanField(default=False, verbose_name="در حال تحصیل")

    class Meta:
        verbose_name = "تحصیلات"
        verbose_name_plural = "تحصیلات"
        ordering = ['-end_date']

    def __str__(self):
        return f"{self.degree} - {self.university}"

class WorkExperience(models.Model):
    # ❌ خطا: objects = None  رو حذف کن
    objects = None
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=100, verbose_name="عنوان شغلی")
    company = models.CharField(max_length=100, verbose_name="شرکت")
    location = models.CharField(max_length=100, verbose_name="موقعیت")
    description = models.TextField(verbose_name="توضیحات")
    start_date = models.DateField(verbose_name="تاریخ شروع")
    end_date = models.DateField(verbose_name="تاریخ پایان", null=True, blank=True)
    is_current = models.BooleanField(default=False, verbose_name="شغل فعلی")

    class Meta:
        verbose_name = "سابقه کاری"
        verbose_name_plural = "سوابق کاری"
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} - {self.company}"

class SkillCategory(models.Model):
    # ❌ خطا: objects = None  رو حذف کن
    objects = None
    name = models.CharField(max_length=50, verbose_name="نام دسته‌بندی")
    icon = models.CharField(max_length=50, verbose_name="آیکون")
    order = models.IntegerField(default=0, verbose_name="ترتیب نمایش")

    class Meta:
        verbose_name = "دسته‌بندی مهارت"
        verbose_name_plural = "دسته‌بندی‌های مهارت"
        ordering = ['order']

    def __str__(self):
        return self.name

class Skill(models.Model):
    # ✅ این مدل درست هست (objects = None نداره)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=50, verbose_name="نام مهارت")
    proficiency = models.IntegerField(
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        default=70,
        verbose_name="میزان تسلط"
    )
    order = models.IntegerField(default=0, verbose_name="ترتیب نمایش")

    class Meta:
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت‌ها"
        ordering = ['order']

    def __str__(self):
        return self.name

class Project(models.Model):
    # ❌ خطا: objects = None  رو حذف کن
    objects = None
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100, verbose_name="عنوان پروژه")
    description = models.TextField(verbose_name="توضیحات")
    technologies = models.CharField(max_length=200, verbose_name="فناوری‌های استفاده شده")
    project_url = models.URLField(blank=True, verbose_name="لینک پروژه")
    github_url = models.URLField(blank=True, verbose_name="لینک گیت‌هاب")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    start_date = models.DateField(verbose_name="تاریخ شروع")
    end_date = models.DateField(verbose_name="تاریخ پایان", null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name="پروژه فعال")

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"
        ordering = ['-start_date']

    def __str__(self):
        return self.title

class SocialMedia(models.Model):
    # ❌ خطا: objects = None  رو حذف کن
    objects = None
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='social_media')
    PLATFORM_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('telegram', 'Telegram'),
        ('email', 'Email'),
        ('twitter', 'Twitter'),
    ]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, verbose_name="پلتفرم")
    url = models.URLField(verbose_name="لینک")
    icon_class = models.CharField(max_length=50, verbose_name="کلاس آیکون")

    class Meta:
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه‌های اجتماعی"

    def __str__(self):
        return self.get_platform_display()

    def get_platform_display(self):
        pass
