class Menu:
  def __init__(self,name, items,start_time,end_time):
    self.name=name
    self.items=items
    self.start_time=start_time
    self.end_time=end_time
  def __repr__(self):
    return self.name +", available from "+ str(self.start_time) +" to "+ str(self.end_time) +"."
  def calculate_bill(self,purchased_items):
    out_bill=0
    for item in purchased_items:
      out_bill+= self.items[item]
    return out_bill
    
items_brunch={
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch=Menu("Brunch",items_brunch,11,16)

items_ebird={
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird=Menu("Early-bird menu",items_ebird,15,18)

items_dinner={
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner=Menu("Dinner",items_dinner,17,23)

items_kids={
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids=Menu("Kids menu",items_kids,11,21)

print(brunch)

#my_order = { key:value for key, value in items_brunch.items() if key =='pancakes' or key == 'home fries' or key == 'coffee' }
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

#We’ve decided to create more than one restaurant to offer our fantastic menus, services, and ambience around the country.
#First, let’s create a Franchise class.
class Franchise:
  def __init__(self,address,menus):
    self.address=address
    self.menus=menus
  def __repr__(self):
    return self.address
  def available_menus(self,time):
    out_menu=[]
    for menu in menus:
      if time >= menu.start_time and time <=menu.end_time:
        out_menu.append(menu)
    return out_menu

#Let’s create our first two franchises! 
menus=[brunch,early_bird,dinner,kids]
flagship_store =Franchise("1232 West End Road",menus)
new_installment =Franchise("12 East Mulberry Street",menus)
print(flagship_store)
print(new_installment)
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

#Since we’ve been so successful building out a branded chain of restaurants, we’ve decided to diversify. 
# We’re going to create a restaurant that sells arepas!
#First let’s define a Business class.
class Business:
  def __init__(self,name,franchises):
    self.name=name
    self.franchises=franchises
    
first_business=Business("Basta Fazoolin' with my Heart",[flagship_store, new_installment])

items_arepa={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepa=Menu("Take a Arepa",items_arepa,10,20)
arepas_place =Franchise("189 Fitzgerald Avenue",[arepa])
new_business=Business("Take a' Arepa",[arepas_place])



