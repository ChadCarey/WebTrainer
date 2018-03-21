import unittest
from Tables import ExerciseType, _Database


class TestExerciseTypesTable(unittest.TestCase):
    def test_add(self):
        ex = ExerciseType(name="cardio")
        _Database.add(ex)
        _Database.commit()
        self.assertTrue(ex.id is not None)

    def test_post_method(self):
        ex_id = ExerciseType.Post(name="Strength")
        self.assertIsNotNone(ex_id)

    # def test_remove(self):
    #     self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
