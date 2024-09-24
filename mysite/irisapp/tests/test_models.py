from django.test import TestCase
from irisApp.models import Iris  # Update the import statement

class IrisModelTest(TestCase):
    def test_iris_creation(self):
        # Create an Iris instance
        iris = Iris.objects.create(
            sepal_length=5.1,
            sepal_width=3.5,
            petal_length=1.4,
            petal_width=0.2,
            species='Setosa'
        )

        # Retrieve the created instance from the database
        saved_iris = Iris.objects.get(species='Setosa')

        # Check if the attributes are set correctly
        self.assertEqual(saved_iris.sepal_length, 5.1)
        self.assertEqual(saved_iris.sepal_width, 3.5)
        self.assertEqual(saved_iris.petal_length, 1.4)
        self.assertEqual(saved_iris.petal_width, 0.2)
        self.assertEqual(saved_iris.species, 'Setosa')
