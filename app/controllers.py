# app/controllers.py
from .models import Category, Item

class GroceryManager:
    def __init__(self, db):
        self.db = db

    def add_category(self, name):
        category = Category(name=name)
        self.db.session.add(category)
        self.db.session.commit()
        print(f"Category '{name}' added successfully.")

    def add_item(self, name, category_id):
        item = Item(name=name, category_id=category_id)
        self.db.session.add(item)
        self.db.session.commit()
        print(f"Item '{name}' added successfully.")

    def delete_category(self, category_id):
        category = self.db.session.query(Category).filter_by(id=category_id).first()
        if category:
            self.db.session.delete(category)
            self.db.session.commit()
            print(f"Category with ID {category_id} deleted successfully.")
        else:
            print(f"Category with ID {category_id} not found.")

    def delete_item(self, item_id):
        item = self.db.session.query(Item).filter_by(id=item_id).first()
        if item:
            self.db.session.delete(item)
            self.db.session.commit()
            print(f"Item with ID {item_id} deleted successfully.")
        else:
            print(f"Item with ID {item_id} not found.")

    def display_all_categories(self):
        categories = self.db.session.query(Category).all()
        if categories:
            for category in categories:
                print(f"Category ID: {category.id}, Name: {category.name}")
        else:
            print("No categories found.")

    def display_all_items(self):
        items = self.db.session.query(Item).all()
        if items:
            for item in items:
                print(f"Item ID: {item.id}, Name: {item.name}, Category ID: {item.category_id}")
        else:
            print("No items found.")

    def find_item_by_name(self, name):
        item = self.db.session.query(Item).filter_by(name=name).first()
        if item:
            print(f"Item found - ID: {item.id}, Name: {item.name}, Category ID: {item.category_id}")
        else:
            print(f"Item with name '{name}' not found.")

