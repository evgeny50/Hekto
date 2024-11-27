import base64
import io

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from matplotlib import pyplot as plt

from core.shop.forms import ProductForm
from core.shop import services
from core.cart.forms import CartAddProductForm
from core.shop.models import Product, Seller, PropertyValue, PropertyKey
from infrastructure.external_services.ai.ai_module import predict_price, avocado_data


def home_page(request):
    featured_products = services.get_featured_products()
    last_product = services.get_last_products()
    return render(request, 'shop/home/home.html', {'featured_products': featured_products,
                                                   'last_product': last_product})


def detail_view_product(request, slug):
    product = services.get_products(slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail_view_product.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def categories_view(request):
    categories = services.get_categories()
    return render(request, 'shop/categories.html', {'categories': categories})


def detail_category(request, slug):
    products = services.get_products_by_category(slug)
    return render(request, 'shop/products_by_category.html', {'products': products})


def get_price_prediction(request):
    if request.method == 'POST':
        data = request.POST

        # Collect necessary data from the request for prediction
        name = data.get('name', 'Avocado')  # Defaulting to 'Avocado' if not provided
        month = int(data.get('month', 6))  # Example field; adjust as needed
        competition = float(data.get('competition', 0.2))
        new_product = int(data.get('new_product', 0))
        popularity = float(data.get('popularity', 0.8))

        # Create a dictionary for new_data that matches the expected format
        new_data = {
            'month': month,
            'category': name,
            'competition': competition,
            'new_product': new_product,
            'popularity': popularity
        }

        # Call the prediction function
        predicted_price = predict_price(new_data)

        # Generate the monthly price trend graph
        plt.figure()
        monthly_avg = avocado_data.groupby('month')['AveragePrice'].mean() * 97
        print(1111111)
        print(monthly_avg)
        monthly_avg.plot(kind='line', marker='o')
        plt.title("Monthly Price Trend")
        plt.xlabel("Month")
        plt.ylabel("Average Price")

        # Save the graph to a buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        graph_url = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        # Return the predicted price and graph URL as JSON
        return JsonResponse({'predicted_price': predicted_price, 'graph_url': graph_url})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def get_property_values(request):
    product_name = request.GET.get('name')
    print(11111)
    print(product_name)
    if product_name:
        products = Product.objects.filter(name__icontains=product_name)  # Найдем все продукты по названию
        properties_data = []

        for product in products:
            # Для каждого продукта собираем свойства
            property_dict = {}

            # Для каждого связанного свойства продукта
            for property_value in product.properties.all():
                print(11111)
                print(product.properties.all())
                property_key_name = property_value.key.name
                property_value_value = property_value.value
                property_key_id = property_value.key.id

                # Если для этого ключа еще нет списка значений, создаем его
                if property_key_id not in property_dict:
                    property_dict[property_key_id] = {
                        'id': property_key_id,
                        'name': property_key_name,
                        'values': []
                    }

                # Добавляем значение в список для данного ключа
                property_dict[property_key_id]['values'].append(property_value_value)

            # Теперь собираем данные из словаря
            for key, data in property_dict.items():
                properties_data.append(data)

        # Печатаем итоговый результат
        result = {"properties": properties_data}
        print(result)

        return JsonResponse({'properties': properties_data})

    return JsonResponse({'properties': []})

@login_required
def create_product(request):
    user = Seller.objects.filter(user=request.user.id).first()
    if not user:
        return JsonResponse({'error': 'Forbidden'}, status=403)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = user
            product.save()
            return redirect('product', slug=product.slug)
    else:
        form = ProductForm()

    return render(request, 'shop/create_product.html', {
        'form': form,
    })

def edit_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product', slug=product.slug)
    else:
        form = ProductForm(instance=product)

    return render(request, 'shop/edit_product.html', {'form': form, 'product': product})



def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        pass
        # product.delete()
        # return redirect('product_list')

    return render(request, 'shop/delete_product.html', {'product': product})


