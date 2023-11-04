
from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return render(request,'notification/index.html')

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'notification/order_list.html', {'orders': orders})


def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            total_orders = Order.objects.count()
            data = {
                'message': 'New order placed - Total order count is {}'.format(total_orders),
                'total_orders': total_orders,
            }
            
            return redirect('order_list')
    else:
        form = OrderForm()

    return render(request, 'notification/add_order.html', {'form': form})



def check_for_new_order(request):
    last_order_id = int(request.GET.get('last_order_id', 0))
    new_order = Order.objects.filter(id__gt=last_order_id).last()
    new_order_id = new_order.id if new_order else last_order_id
    return JsonResponse({'new_order_id': new_order_id})

