import unittest
from cake_factory import CakeFactory

class TestCakeFactory(unittest.TestCase):

    def test_create_cake(self):
        """Test cake creation with default attributes."""
        cake = CakeFactory("vanilla", "small")
        self.assertEqual(cake.cake_type, "vanilla")
        self.assertEqual(cake.size, "small")
        self.assertEqual(cake.price, 8)  

    def test_add_topping(self):
        """Test if toppings are added correctly."""
        cake = CakeFactory("chocolate", "large")
        cake.add_topping("sprinkles")
        self.assertIn("sprinkles", cake.toppings)

    def test_check_ingredients(self):
        """Test if the correct ingredients are returned."""
        cake = CakeFactory("chocolate", "medium")
        cake.add_topping("cherries")
        ingredients = cake.check_ingredients()
        self.assertIn("cocoa", ingredients)
        self.assertIn("cherries", ingredients)
        self.assertNotIn("vanilla extract", ingredients)  

    def test_check_price(self):
        """Test if the price calculation is correct."""
        cake = CakeFactory("vanilla", "large")
        cake.add_topping("sprinkles")
        cake.add_topping("cherries")
        price = cake.check_price()
        self.assertEqual(price, 14)  
        
if __name__ == "__main__":
    unittest.main()
