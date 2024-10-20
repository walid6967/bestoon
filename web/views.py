import json
from web.models import User, Expense, Income
from datetime import datetime
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.db import models

@csrf_exempt
def expense(request):
    try:
        data = json.loads(request.body)
        this_token = data.get('token')
        if not this_token:
            return JsonResponse({'status': 'error', 'message': 'Token missing'}, status=400)

        this_user = User.objects.filter(token__token=this_token).get()
        date = data.get('date', datetime.now())
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, '%Y/%m/%d')
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
        this_token = data.get('token')
        if not this_token:
            return JsonResponse({'status': 'error', 'message': 'Token missing'}, status=400)

        this_user = User.objects.filter(token__token=this_token).get()
        date = data.get('date', datetime.now())
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, '%Y/%m/%d')
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
    
@csrf_exempt
def balance(request):
    try:
        data = json.loads(request.body)
        this_token = data.get('token')
        if not this_token:
            return JsonResponse({'status': 'error', 'message': 'Token missing'}, status=400)
        this_user = User.objects.filter(token__token=this_token).get()
        total_income = Income.objects.filter(user=this_user).aggregate(total_income=models.Sum('amount'))['total_income'] or 0
        total_expenses = Expense.objects.filter(user=this_user).aggregate(total_expense=models.Sum('amount'))['total_expense'] or 0
        remaining_balance = total_income - total_expenses

        return JsonResponse({
            'status': 'success',
            'total_income': total_income,
            'total_expenses': total_expenses,
            'balance': remaining_balance
        }, encoder=JSONEncoder, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Invalid token or user not found'}, status=404)