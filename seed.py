#!/usr/bin/env python3
"""
Seed script to populate the database with initial menu items for Timeless Sip.
Usage:
  python seed.py
"""
from app import create_app, db
from app.models import MenuItem

app = create_app()

# Sample menu items to seed
def get_seed_items():
    return [
        # Coffees
        MenuItem(
            name="Espresso",
            price=45,
            category="Coffees",
            description="Strong, rich coffee shot in a small cup."
        ),
        MenuItem(
            name="Americano",
            price=50,
            category="Coffees",
            description="Espresso diluted with hot water for a smooth flavor."
        ),
        MenuItem(
            name="Latte",
            price=60,
            category="Coffees",
            description="Steamed milk with a shot of espresso, creamy and mild."
        ),
        MenuItem(
            name="Cappuccino",
            price=65,
            category="Coffees",
            description="Espresso topped with steamed and foamed milk."
        ),
        MenuItem(
            name="Flat White",
            price=70,
            category="Coffees",
            description="Velvety steamed milk with a double shot of espresso."
        ),
        # Desserts
        MenuItem(
            name="Chocolate Cake",
            price=85,
            category="Desserts",
            description="Rich, moist chocolate cake topped with ganache."
        ),
        MenuItem(
            name="Cheesecake",
            price=95,
            category="Desserts",
            description="Creamy cheesecake with a graham cracker crust."
        ),
        MenuItem(
            name="Apple Strudel",
            price=75,
            category="Desserts",
            description="Thin pastry filled with spiced apples."
        ),
        MenuItem(
            name="Tiramisu",
            price=90,
            category="Desserts",
            description="Classic Italian dessert with coffee and mascarpone."
        ),
        MenuItem(
            name="Brownie",
            price=50,
            category="Desserts",
            description="Fudgy chocolate brownie square."
        ),
        # Pastries
        MenuItem(
            name="Croissant",
            price=35,
            category="Pastries",
            description="Buttery, flaky French pastry."
        ),
        MenuItem(
            name="Cinnamon Roll",
            price=40,
            category="Pastries",
            description="Sweet roll with cinnamon and icing."
        ),
        MenuItem(
            name="Pain au Chocolat",
            price=45,
            category="Pastries",
            description="Flaky pastry with chocolate filling."
        ),
        MenuItem(
            name="Blueberry Muffin",
            price=50,
            category="Pastries",
            description="Moist muffin studded with blueberries."
        ),
        MenuItem(
            name="Butter Scone",
            price=30,
            category="Pastries",
            description="Tender scone perfect with jam and cream."
        ),
        # Beverages
        MenuItem(
            name="Mineral Water",
            price=25,
            category="Beverages",
            description="Chilled mineral water."
        ),
        MenuItem(
            name="Fresh Orange Juice",
            price=40,
            category="Beverages",
            description="Cold-pressed fresh orange juice."
        ),
        MenuItem(
            name="Iced Tea",
            price=35,
            category="Beverages",
            description="Refreshing iced tea with optional lemon."
        ),
        MenuItem(
            name="Hot Chocolate",
            price=50,
            category="Beverages",
            description="Rich, creamy hot chocolate."
        ),
        MenuItem(
            name="Herbal Tea",
            price=30,
            category="Beverages",
            description="Selection of soothing herbal infusions."
        ),
    ]

if __name__ == '__main__':
    with app.app_context():
        # Ensure all tables exist
        db.create_all()

        count = MenuItem.query.count()
        if count > 0:
            print(f"Database already seeded with {count} items.")
        else:
            items = get_seed_items()
            db.session.bulk_save_objects(items)
            db.session.commit()
            print(f"Seeded {len(items)} menu items.")