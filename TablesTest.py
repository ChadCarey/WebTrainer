import unittest
from Tables import ExerciseType, Database


class TestExerciseTypesTable(unittest.TestCase):
    def test_add(self):
        ex = ExerciseType(name="cardio")
        Database.add(ex)
        Database.commit()
        self.assertTrue(ex.id is not None)

    # def test_remove(self):
    #     self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
