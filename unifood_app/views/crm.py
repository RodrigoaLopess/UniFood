from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from unifood_app.models import Pedido, Produto


@login_required
def dashboard(request):
    total_pedidos = Pedido.objects.filter(vendedor=request.user).count()
    total_produtos = Produto.objects.filter(vendedor=request.user).count()
    total_clientes = (
        Pedido.objects.filter(vendedor=request.user)
        .values('cliente')
        .distinct()
        .count()
    )

    context = {
        'total_pedidos': total_pedidos,
        'total_produtos': total_produtos,
        'total_clientes': total_clientes,
    }
    return render(request, 'unifood_app/crm/dashboard.html', context)
