from django.db import models

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability_status = models.BooleanField(default=True)

    class Meta:
        db_table = 'rooms'

        def __str__(self):
            return f"{self.room_id} - {self.type}({'Available' if self.availability_status else 'Occupied'})"

