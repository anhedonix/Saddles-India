from django.db import models
from django.utils import timezone

class Color(models.Model):
    author = models.ForeignKey('auth.User')
    label = models.CharField(max_length=200)
    #category = models.CharField(max_length=200, blank=True)
    #sub_category = models.CharField(max_length=200, blank=True)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    col_l = models.FloatField()
    col_a = models.FloatField()
    col_b = models.FloatField()

    R = models.FloatField(editable=False)
    G = models.FloatField(editable=False)
    B = models.FloatField(editable=False)

    Hex = models.CharField(editable=False, max_length=6)

    def save(self, *args, **kwargs):

        var_Y = ( self.col_l + 16 ) / 116
        var_X = self.col_a / 500 + var_Y
        var_Z = var_Y - self.col_b / 200

        if ( var_Y**3 > 0.008856 ):
            var_Y = var_Y**3
        else:
            var_Y = ( var_Y - 16 / 116 ) / 7.787

        if ( var_X**3 > 0.008856 ):
            var_X = var_X**3
        else:
            var_X = ( var_X - 16 / 116 ) / 7.787

        if ( var_Z**3 > 0.008856 ):
            var_Z = var_Z**3
        else:
            var_Z = ( var_Z - 16 / 116 ) / 7.787

        ref_X =  95.047     #Observer= 2°, Illuminant= D65
        ref_Y = 100.000
        ref_Z = 108.883

        var_X = (ref_X * var_X) / 100       #X from 0 to  95.047      (Observer = 2°, Illuminant = D65)
        var_Y = (ref_Y * var_Y) / 100       #Y from 0 to 100.000
        var_Z = (ref_Z * var_Z) / 100       #Z from 0 to 108.883

        var_R = var_X *  3.2406 + var_Y * -1.5372 + var_Z * -0.4986
        var_G = var_X * -0.9689 + var_Y *  1.8758 + var_Z *  0.0415
        var_B = var_X *  0.0557 + var_Y * -0.2040 + var_Z *  1.0570

        if ( var_R > 0.0031308 ):
            var_R = 1.055 * ( var_R ** ( 1 / 2.4 ) ) - 0.055
        else:
            var_R = 12.92 * var_R

        if ( var_G > 0.0031308 ):
            var_G = 1.055 * ( var_G ** ( 1 / 2.4 ) ) - 0.055
        else:
            var_G = 12.92 * var_G

        if ( var_B > 0.0031308 ):
            var_B = 1.055 * ( var_B ** ( 1 / 2.4 ) ) - 0.055
        else:
            var_B = 12.92 * var_B

        R = var_R
        G = var_G
        B = var_B

        self.R = R      #calculation
        self.G = G      #calculation
        self.B = B      #calculation

        self.Hex = '%02x%02x%02x' % (self.R*255, self.G*255, self.B*255)

        super(Color, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.label