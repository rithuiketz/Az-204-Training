from services.DBService import DBService
from datetime import datetime
from orm.Entity import Category, SKU, SKUBrand, Seller

class InventoryData():

    def __init__(self):
        self.db_svc =  DBService()
        
    def initData(self):
        category = Category(cat_name="Electronics", cat_desc="Electronic items")
        self.db_svc.persist_obj(category)
        brand = SKUBrand(brand_name="Samsung", brand_desc="Samsung electronics")
        self.db_svc.persist_obj(brand)
        seller = Seller(
        fname="John", lname="Doe", mobile="1234567890", address="123 Street Name"
        )
        self.db_svc.persist_obj(seller)
        sku = SKU(
        sku_name="Samsung TV",
        sku_desc="Smart TV 4K",
        is_active=True,
        category=category,
        brand=brand,
        seller=seller)
        self.db_svc.persist_obj(sku)
    

    

        
