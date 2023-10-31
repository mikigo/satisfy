from django.db import models
from django.utils import timezone


# Create your models here.


class Location(models.Model):
    class Meta:
        db_table = "location"
        verbose_name = verbose_name_plural = "获取坐标"

    amd = "amd"
    arm = "arm"
    archs = (
        (amd, "amd64"),
        (arm, "arm64"),
    )
    create_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    class_name = models.CharField(verbose_name="类名称", max_length=255, null=False)
    func_name = models.CharField(verbose_name="函数名称", max_length=255, null=False)
    args = models.CharField(verbose_name="参数", max_length=255, null=True, blank=True)
    sys_arch = models.CharField(verbose_name="系统架构", max_length=255, choices=archs, default=amd)
    px = models.CharField(verbose_name="分辨率", max_length=255, null=False)
    location_x = models.FloatField(verbose_name="横坐标", null=False)
    location_y = models.FloatField(verbose_name="纵坐标", null=False)
