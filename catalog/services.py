from config.settings import CACHE_ENABLE
from catalog.models import Product
from django.core.cache import cache

class ProductService:

    @staticmethod
    def get_products_from_cache():
        """ Метод получения данных из кеша, если кеш - None, то получается данные из БД. """
        if not CACHE_ENABLE:
            return Product.objects.all()

        key = 'product_list'
        products = cache.get(key)

        if products is not None:
            return products

        products = Product.objects.all()
        cache.set(key, products)

        return products

    @staticmethod
    def get_products_by_category_cache(category_id):
        """ Метод для получения продуктов по категориям используя кеш. """
        products = ProductService.get_products_from_cache()
        category_products = products.filter(category=category_id)

        if not category_products.exists():
            return None

        return category_products
