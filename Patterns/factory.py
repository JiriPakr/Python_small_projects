
# Example 1 - burger Factory
class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

class BurgerFartory:

    def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "beef"]
        return Burger(ingredients)
    
    def createDeluxeCheeseBurger(self):
        ingredients = ["bun", "tomato", "lettuce", "cheese", "beef"]
        return Burger(ingredients)
    
    def createVeganBurger(self):
        ingredients = ["bun", "special-sauce", "not-meat"]
        return Burger(ingredients)

##########################################################

burgerFartory = BurgerFartory()
burgerFartory.createCheeseBurger().print()
burgerFartory.createDeluxeCheeseBurger().print()
burgerFartory.createVeganBurger().print()