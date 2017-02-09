
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math


class Color(models.Model):

    label = models.CharField(max_length=200)
    category = models.ForeignKey('Category', verbose_name="Category", on_delete=models.CASCADE, help_text = "What category does this leather come under? Ex: Napa, Exports.")
    tags = models.ManyToManyField('Tag', verbose_name="Tags", help_text = "What can this leather be described as? Ex: Tan, Beige, Black, Mud.")

    description = models.CharField(blank=True, null=True,max_length=200, help_text = "Any additional details about the leather sample that might help identify it, or the reason for its scanning.")

    created_date = models.DateTimeField(default=timezone.now, editable=False)
    published_date = models.DateTimeField(blank=True, null=True, editable=False)


    col_l = models.FloatField(verbose_name="L")
    col_a = models.FloatField(verbose_name=" a")
    col_b = models.FloatField(verbose_name=" b")
    col_c = models.FloatField(verbose_name="C")
    col_h = models.FloatField(verbose_name=" h")

    R = models.FloatField(blank=True, null=True)
    G = models.FloatField(blank=True, null=True)
    B = models.FloatField(blank=True, null=True)

    R1 = models.FloatField(blank=True, null=True)
    G1 = models.FloatField(blank=True, null=True)
    B1 = models.FloatField(blank=True, null=True)

    R2 = models.FloatField(blank=True, null=True)
    G2 = models.FloatField(blank=True, null=True)
    B2 = models.FloatField(blank=True, null=True)

    H = models.FloatField(editable=False, blank=True, null=True)
    S = models.FloatField(editable=False, blank=True, null=True)
    V = models.FloatField(editable=False, blank=True, null=True)

    Hex = models.CharField(blank=True, null=True, max_length=6)

    def save(self, *args, **kwargs):

        var_Y1 = ( self.col_l + 16 ) / 116
        var_X1 = self.col_a / 500 + var_Y1
        var_Z1 = var_Y1 - self.col_b / 200

        if ( var_Y1**3 > 0.008856 ):
            var_Y1 = var_Y1**3
        else:
            var_Y1 = ( var_Y1 - 16 / 116 ) / 7.787

        if ( var_X1**3 > 0.008856 ):
            var_X1 = var_X1**3
        else:
            var_X1 = ( var_X1 - 16 / 116 ) / 7.787

        if ( var_Z1**3 > 0.008856 ):
            var_Z1 = var_Z1**3
        else:
            var_Z1 = ( var_Z1 - 16 / 116 ) / 7.787

        ref_X =  95.047
        ref_Y = 100.000
        ref_Z = 108.883

        var_X1 = (ref_X * var_X1) / 100       #X from 0 to  95.047
        var_Y1 = (ref_Y * var_Y1) / 100       #Y from 0 to 100.000
        var_Z1 = (ref_Z * var_Z1) / 100       #Z from 0 to 108.883

        var_R1 = var_X1 *  3.2406 + var_Y1 * -1.5372 + var_Z1 * -0.4986
        var_G1 = var_X1 * -0.9689 + var_Y1 *  1.8758 + var_Z1 *  0.0415
        var_B1 = var_X1 *  0.0557 + var_Y1 * -0.2040 + var_Z1 *  1.0570

        if ( var_R1 > 0.0031308 ):
            var_R1 = 1.055 * ( var_R1 ** ( 1 / 2.4 ) ) - 0.055
        else:
            var_R1 = 12.92 * var_R1

        if ( var_G1 > 0.0031308 ):
            var_G1 = 1.055 * ( var_G1 ** ( 1 / 2.4 ) ) - 0.055
        else:
            var_G1 = 12.92 * var_G1

        if ( var_B1 > 0.0031308 ):
            var_B1 = 1.055 * ( var_B1 ** ( 1 / 2.4 ) ) - 0.055
        else:
            var_B1 = 12.92 * var_B1

        col_l2 = self.col_l
        col_a2 = math.cos( math.radians( self.col_h ) ) * self.col_c
        col_b2 = math.sin( math.radians( self.col_h ) ) * self.col_c


        var_Y2 = ( col_l2 + 16 ) / 116
        var_X2 = col_a2 / 500 + var_Y2
        var_Z2 = var_Y2 - col_b2 / 200

        if ( var_Y2**3 > 0.008856 ):
            var_Y2 = var_Y2**3
        else:
            var_Y2 = ( var_Y2 - 16 / 116 ) / 7.787

        if ( var_X2**3 > 0.008856 ):
            var_X2 = var_X2**3
        else:
            var_X2 = ( var_X2 - 16 / 116 ) / 7.787

        if ( var_Z2**3 > 0.008856 ):
            var_Z2 = var_Z2**3
        else:
            var_Z2 = ( var_Z2 - 16 / 116 ) / 7.787

        ref_X =  95.047
        ref_Y = 100.000
        ref_Z = 108.883

        var_X2 = (ref_X * var_X2) / 100       #X from 0 to  95.047
        var_Y2 = (ref_Y * var_Y2) / 100       #Y from 0 to 100.000
        var_Z2 = (ref_Z * var_Z2) / 100       #Z from 0 to 108.883

        var_R2 = var_X2 *  3.2406 + var_Y2 * -1.5372 + var_Z2 * -0.4986
        var_G2 = var_X2 * -0.9689 + var_Y2 *  1.8758 + var_Z2 *  0.0415
        var_B2 = var_X2 *  0.0557 + var_Y2 * -0.2040 + var_Z2 *  1.0570

        if ( var_R2 > 0.0031308 ):
            var_R2 = 1.055 * ( var_R2 ** ( 1 / 2.4 ) ) - 0.055
        else:
            var_R2 = 12.92 * var_R2

        if ( var_G2 > 0.0031308 ):
            var_G2 = 1.055 * ( var_G2 ** ( 1 / 2.4 ) ) - 0.055
        else:
            var_G2 = 12.92 * var_G2

        if ( var_B2 > 0.0031308 ):
            var_B2 = 1.055 * ( var_B2 ** ( 1 / 2.4 ) ) - 0.055
        else:
            var_B2 = 12.92 * var_B2

        R1 = var_R1
        G1 = var_G1
        B1 = var_B1
        R2 = var_R2
        G2 = var_G2
        B2 = var_B2
        # R2 = var_Y2
        # G2 = var_X2
        # B2 = var_Z2

        self.R1 = R1
        self.G1 = G1
        self.B1 = B1

        self.R2 = R2
        self.G2 = G2
        self.B2 = B2

        self.R = (R1 + R2)/2
        self.G = (G1 + G2)/2
        self.B = (B1 + B2)/2

        self.Hex = '%02x%02x%02x' % (self.R*255, self.G*255, self.B*255)

        self.published_date = timezone.now()

        #self.author = request.user

        super(Color, self).save(*args, **kwargs)


    def __str__(self):
        return self.label

    def new(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=3)

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Category")

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tag")

    def __str__(self):
        return self.title
