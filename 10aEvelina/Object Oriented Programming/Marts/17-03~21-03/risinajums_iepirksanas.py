
#1. uzdevums - A, B, C
class Product:      #A
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):  #B
        return self.price * self.quantity

#2. uzdevums - D, E, F, G
class ShoppingCart: #D
    def __init__(self):
        self.items = []

    def add_product_to_cart(self, product: Product): #E
        self.items.append(product)
        print(f"Produkts '{product.name}' pievienots grozam.")
        
    def remove_product_from_cart(self, product: Product):
        self.items.remove(product)
        print(f"Produkts '{product.name}' izņemts no groza.")
    
    def get_total_price(self):
        total_price = 0.00
        for item in self.items:
            total_price += item.get_total_price()
        return total_price

#3. uzdevums - H, I, J, K
class SystemUser(): #H
    def __init__(self, username: str, password: str, email: str): #I
        self.username = username
        self.password = password
        self.email = email

    def set_user_info(self, newusername: str, newpassword: str, newemail: str): #J
        self.username = newusername
        self.password = newpassword
        self.email = newemail   
        print("Informācija ir nomainīta!")  

    def get_user_info(self): #J
        print(f'Lietotājvārds: {self.username}\nE-pasts: {self.email}\nParole: {self.password}')

#4. uzdevums - L, M, N
class Customer(SystemUser): #L
    def __init__(self, username: str, password: str, email: str, customer_id: str, purchase_history: list, membership_status: bool): #M
        super().__init__(username, password, email)
        self.customer_id = customer_id
        self.purchase_history = purchase_history
        self.membership_status = membership_status

    def set_user_info(self, newusername: str, newpassword: str, newemail: str, newcustomer_id: str, newpurchase_history: list, newmembership_status: bool):
        super().set_user_info(newusername, newpassword, newemail) #M
        self.customer_id = newcustomer_id
        self.purchase_history = newpurchase_history
        self.membership_status = newmembership_status
    
    def get_user_info(self):
        super().get_user_info()
        print(f'Klienta ID: {self.customer_id}\nPirkumu vēsture: {self.purchase_history}')
        print(f"Ir lojalitātes programma: {'Jā' if self.membership_status else 'Nē'}")


gurki = Product("Marinēti Gurķi", 6.50, 3)    #C
dibeles = Product("Dībeles", 2, 6)
print("\n")
print(f'Cena {gurki.name}, {gurki.quantity} gab: {gurki.get_total_price()}€')
print(f'Cena {dibeles.name}, {dibeles.quantity} gab: {dibeles.get_total_price()}€')
print('*' * 30)


cart = ShoppingCart() #F
cart.add_product_to_cart(gurki)
cart.add_product_to_cart(dibeles) #G

print(f'Cena iepirkšanās grozam: {cart.get_total_price()}€')
print('*' * 30)

cart.remove_product_from_cart(gurki)
cart.remove_product_from_cart(dibeles)

print(f'Cena iepirkšanās grozam: {cart.get_total_price()}€')
print('*' * 30)


user = SystemUser("anna_kalnina", "esMiluKakisus35", "anna@gmail.com") #K
user.get_user_info()
print('*' * 30)

user.set_user_info("janis_berzins", "ManPatikSuni28", "janis@gmail.com")
user.get_user_info()
print('*' * 30)


#O
customer = Customer('klients', 'xyz123', 'klients@veikals.lv', '000000001', [], False)
customer.get_user_info()
print('*' * 30)

customer.set_user_info('pircejs', '321zyx', 'pircejs@1a.lv', '111111110', ["Āboli, Dībeles"], True)
customer.get_user_info()
print('*' * 30)
