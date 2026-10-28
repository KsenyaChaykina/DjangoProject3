from django.shortcuts import get_object_or_404

from config.settings import CACHE_ENABLED
from catalog.models import Product, Category
from django.core.cache import cache


def get_products_from_cache():
    """ Получает данные по продуктам из кеша, если кеш пуст, получает данные из бд и записывает в кеш """
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return  products

def get_products_by_category(category_id):
    """ Возвращает список всех продуктов в указанной категории """
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    return category, products