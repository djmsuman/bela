from celery.result import AsyncResult
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Item
from ..serializers import ItemSerializer
from ..tasks import notify_item_added


class ItemsView(APIView):
    """
    View to list all items and create a new item.
    """

    def get(self, request):
        """
        List all items.
        """
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new item.
        """
        serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            # Trigger the Celery task to notify that an item has been added
            result = notify_item_added.delay(
                serializer.data["id"],
                serializer.data["name"],
                serializer.data["description"],
            )

            return Response(
                {
                    "item": serializer.data,
                    "task_id": result.id,
                },
                status=201,
            )
        return Response(serializer.errors, status=400)


class ItemNotificationStatusView(APIView):
    """
    View to check the status of the item notification task.
    """

    def get(self, request, task_id):
        """
        Get the status of the notification task.
        """
        result = AsyncResult(task_id)

        if result.state == "PENDING":
            response = {"state": result.state, "status": "Task is still pending."}
        elif result.state != "FAILURE":
            response = {"state": result.state, "result": result.result}
        else:
            # something went wrong in the background job
            response = {
                "state": result.state,
                "status": str(result.info),  # this is the exception raised
            }
        return Response(response)
