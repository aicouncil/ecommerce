from ecommerce.products.product_manager import add_product, list_products
from ecommerce.users.user_manager import add_user,list_users
from ecommerce.orders.order_manger import create_order,list_orders

#Adding products
add_product("Laptop",1200,10)
add_product("SmartPhone",800,20)
list_products()

#Adding users
add_user("John Doe" , "johndoe@example.com")
list_users()


#Creating orders
create_order("JohnDoe","Laptop",1)
list_orders()
