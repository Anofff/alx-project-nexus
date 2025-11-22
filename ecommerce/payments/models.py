import uuid
from django.db import models
from users.models import User
from orders.models import Order


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="payments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payments"
    )

    amount = models.FloatField()
    reference = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    paid_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.reference}"
