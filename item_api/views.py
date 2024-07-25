# item_api/views.py
from django.http import JsonResponse


def get_aliexpress_item_name_view(request):
    if request.method == 'GET':
        item_id = request.GET.get('item_id')  # Assuming the item_id is passed as a query parameter
        return JsonResponse({'item_name': item_id})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
