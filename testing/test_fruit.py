import pytest

class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True

class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()

@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act: Create a FruitSalad instance
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert: Check if all fruits are cubed
    assert all(fruit.cubed for fruit in fruit_salad.fruit)
