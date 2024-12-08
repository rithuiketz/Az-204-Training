from qcomm_invmgmt.services.DBService import DBService
from datetime import datetime
from qcomm_invmgmt.orm.Entity import Category, SKU, SKUBrand, Seller

class InventoryData():

    def __init__(self):
        self.db_svc =  DBService()
        
    def initData(self):
        category = [Category(cat_name="Electronics", cat_desc="Electronic items")]
        self.db_svc.persist_obj_list(category)
        
        brand =  [SKUBrand(brand_name="Samsung", brand_desc="Samsung electronics")]
        self.db_svc.persist_obj_list(brand)
        
        seller =[Seller(
                    fname="John1", lname="Doe1", mobile="1234567890", address="123 Street Name"
        )]
        self.db_svc.persist_obj_list(seller)


        sku = SKU(
        sku_name="Samsung TV",
        sku_desc="Smart TV 4K",
        is_active=True,
        category=category[0],
        brand=brand[0],
        seller=seller[0])
        
        self.db_svc.persist_obj(sku)
    
class TemplateGenerator():

    def writeFile(self):
        cols = ["SKU NAME,SKU DESC,CATEGORY,BRAND,SELLER_ID"]
        rows =[
                "T SHIRT BLUE XL,T SHIRT OF XL SIZE,APPEARNCES & WEARABLE,LP,89b7fcfb-b2f3-4c7f-8cf5-e43d8dfc29e1",
                "FOSSIL WATCH,DESC,APPEARNCES & WEARABLE,FOSSIL,89b7fcfb-b2f3-4c7f-8cf5-e43d8dfc29e1"
            ]
        str_data = cols[0]
        for row in rows:
            str_data+="\n"
            str_data+=row
        return str_data