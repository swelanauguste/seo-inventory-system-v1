from suppliers.models import Category, Supplier


def supplier_categories(request):
    return {"supplier_category_list": Category.objects.all().order_by("slug")}

