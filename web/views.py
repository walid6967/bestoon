import json
from django.shortcuts import render
from web.models import User, Expense, Income
from datetime import datetime
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def expense(request):
    try:
        data = json.loads(request.body)
        this_token = data.get('token')  # Get token safely
        if not this_token:
            return JsonResponse({'status': 'error', 'message': 'Token missing'}, status=400)

        this_user = User.objects.filter(token__token=this_token).get()
        date = data.get('date', datetime.now())
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, '%Y/%m/%d')  # Example date format '1403/1/1'
            except ValueError:
                return JsonResponse({'status': 'error', 'message': 'Invalid date format'}, status=400)
        Expense.objects.create(
            user=this_user,
            date=date,
            amount=data.get('amount'),
            text=data.get('text')
        )
        return JsonResponse({'Expense': data}, encoder=JSONEncoder, status=201)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Invalid token or user not found'}, status=404)
    
@csrf_exempt
def income(request):
    try:
        data = json.loads(request.body)
        this_token = data.get('token')  # Get token safely
        if not this_token:
            return JsonResponse({'status': 'error', 'message': 'Token missing'}, status=400)

        this_user = User.objects.filter(token__token=this_token).get()
        date = data.get('date', datetime.now())
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, '%Y/%m/%d')  # Example date format '1403/1/1'
            except ValueError:
                return JsonResponse({'status': 'error', 'message': 'Invalid date format'}, status=400)
        Income.objects.create(
            user=this_user,
            date=date,
            amount=data.get('amount'),
            text=data.get('text')
        )
        return JsonResponse({'Income': data}, encoder=JSONEncoder, status=201)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Invalid token or user not found'}, status=404)