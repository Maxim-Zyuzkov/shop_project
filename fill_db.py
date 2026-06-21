import os
import django

# Настраиваем окружение Django для работы скрипта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')
django.setup()

from shop.models import Category, Manufacturer, Product
import random

def create_data():
    print("Начинаем заполнение базы данных...")

    # 1. Создаём 3 категории (по теме твоего магазина)
    categories_data = [
        {"name": "Куртки и пуховики", "description": "Защита от ветра, дождя и холода для активного отдыха."},
        {"name": "Головные уборы", "description": "Кепки, шапки и балаклавы для любой погоды."},
        {"name": "Термобельё", "description": "Сохраняет тепло и отводит влагу для комфорта."},
    ]
    
    created_categories = []
    for cat_data in categories_data:
        cat, created = Category.objects.get_or_create(
            name=cat_data["name"],
            defaults={"description": cat_data["description"]}
        )
        created_categories.append(cat)
        if created:
            print(f"  ✅ Создана категория: {cat.name}")
        else:
            print(f"  ➡️ Категория уже есть: {cat.name}")

    # 2. Создаём 5 производителей
    manufacturers_data = [
        {"name": "Columbia", "country": "США", "description": "Американский бренд спортивной одежды."},
        {"name": "The North Face", "country": "США", "description": "Снаряжение для экстремальных путешествий."},
        {"name": "Adidas Terrex", "country": "Германия", "description": "Линейка для активного отдыха."},
        {"name": "Nike ACG", "country": "США", "description": "All Conditions Gear — для любых условий."},
        {"name": "Stayer", "country": "Россия", "description": "Отечественный бренд качественной экипировки."},
    ]
    
    created_manufacturers = []
    for man_data in manufacturers_data:
        man, created = Manufacturer.objects.get_or_create(
            name=man_data["name"],
            defaults={
                "country": man_data["country"],
                "description": man_data["description"]
            }
        )
        created_manufacturers.append(man)
        if created:
            print(f"  ✅ Создан производитель: {man.name}")
        else:
            print(f"  ➡️ Производитель уже есть: {man.name}")

    # 3. Создаём 30 товаров (первые 15 + вторые 15)
    product_templates = [
        # ================= ПЕРВАЯ ПАРТИЯ (15 товаров) =================
        {"name": "Тёплая куртка Columbia", "desc": "Водонепроницаемая мембрана, утеплитель Omni-Heat.", "price": 18990, "cat": 0},
        {"name": "Пуховик The North Face", "desc": "Натуральный пух, лёгкий и тёплый.", "price": 24990, "cat": 0},
        {"name": "Трекинговая куртка Adidas Terrex", "desc": "Дышащая ткань, защита от ветра.", "price": 15990, "cat": 0},
        {"name": "Куртка Nike ACG", "desc": "Стиль и функциональность для города.", "price": 13990, "cat": 0},
        {"name": "Парка Stayer", "desc": "Очень тёплая парка для суровых зим.", "price": 21990, "cat": 0},
        {"name": "Кепка Columbia", "desc": "Защита от солнца, регулируемый размер.", "price": 2990, "cat": 1},
        {"name": "Бейсболка The North Face", "desc": "Классическая кепка с логотипом.", "price": 3490, "cat": 1},
        {"name": "Шапка Adidas Terrex", "desc": "Тёплая вязаная шапка для трекинга.", "price": 2490, "cat": 1},
        {"name": "Балаклава Nike ACG", "desc": "Защита лица и шеи от ветра.", "price": 1990, "cat": 1},
        {"name": "Кепка Stayer", "desc": "Спортивная кепка с сеткой.", "price": 1890, "cat": 1},
        {"name": "Термобельё Columbia", "desc": "Набор (футболка + штаны), дышащее.", "price": 7990, "cat": 2},
        {"name": "Термофутболка The North Face", "desc": "Базовый слой, быстро сохнет.", "price": 4990, "cat": 2},
        {"name": "Термоштаны Adidas Terrex", "desc": "Для активных тренировок на холоде.", "price": 5990, "cat": 2},
        {"name": "Термобельё Nike ACG", "desc": "Лёгкое, отводит влагу.", "price": 6990, "cat": 2},
        {"name": "Термокомплект Stayer", "desc": "Идеально для рыбалки и охоты.", "price": 5490, "cat": 2},

        # ================= ВТОРАЯ ПАРТИЯ (ещё 15 товаров) =================
        # Куртки (категория 0)
        {"name": "Куртка-дождевик Columbia", "desc": "Лёгкая непромокаемая куртка для путешествий.", "price": 8990, "cat": 0},
        {"name": "Ветровка The North Face", "desc": "Тонкая ветрозащитная куртка для бега.", "price": 10990, "cat": 0},
        {"name": "Горная куртка Adidas", "desc": "Прочная ткань, защита от скал.", "price": 18990, "cat": 0},
        {"name": "Urban куртка Nike", "desc": "Современный дизайн для города.", "price": 12990, "cat": 0},
        {"name": "Парка Stayer Premium", "desc": "Усиленная парка с капюшоном.", "price": 25990, "cat": 0},
        # Головные уборы (категория 1)
        {"name": "Панама Columbia", "desc": "Защита от солнца для пляжа и походов.", "price": 1990, "cat": 1},
        {"name": "Шапка-бини The North Face", "desc": "Стильная вязаная шапка.", "price": 2590, "cat": 1},
        {"name": "Кепка Adidas", "desc": "Спортивная кепка с логотипом.", "price": 2190, "cat": 1},
        {"name": "Шапка Nike", "desc": "Утеплённая шапка для зимы.", "price": 2890, "cat": 1},
        {"name": "Балаклава Stayer", "desc": "Тёплая балаклава для морозов.", "price": 1490, "cat": 1},
        # Термобельё (категория 2)
        {"name": "Термобельё Columbia Light", "desc": "Лёгкий набор для весны.", "price": 6990, "cat": 2},
        {"name": "Термобельё The North Face Pro", "desc": "Профессиональная серия.", "price": 8990, "cat": 2},
        {"name": "Термоноски Adidas", "desc": "Тёплые носки для трекинга.", "price": 1190, "cat": 2},
        {"name": "Термобельё Nike", "desc": "Базовый слой для бега.", "price": 5990, "cat": 2},
        {"name": "Термобельё Stayer", "desc": "Набор из футболки и кальсон.", "price": 4790, "cat": 2},
    ]

    products_count = 0
    for template in product_templates:
        # Выбираем категорию из списка созданных
        category = created_categories[template["cat"]]
        # Рандомно выбираем производителя
        manufacturer = random.choice(created_manufacturers)
        
        # Создаём товар (если такого названия ещё нет)
        obj, created = Product.objects.get_or_create(
            name=template["name"],
            defaults={
                "description": template["desc"],
                "price": template["price"],
                "stock": random.randint(5, 20),  # Склад: от 5 до 20 штук
                "category": category,
                "manufacturer": manufacturer
            }
        )
        if created:
            products_count += 1
            print(f"  ✅ Создан товар: {obj.name} (Цена: {obj.price}₽)")

    print("\n" + "="*50)
    print(f"🎉 Готово! Создано:")
    print(f"   - {len(created_categories)} категории")
    print(f"   - {len(created_manufacturers)} производителей")
    print(f"   - {products_count} товаров (из них 15 новых)")
    print("="*50)

if __name__ == "__main__":
    create_data()