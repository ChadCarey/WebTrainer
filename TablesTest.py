import unittest
from Tables import ExerciseType


class TestExerciseTypesTable(unittest.TestCase):

    def test_ExerciseType_post_method_adds_item_to_database(self):
        ex = ExerciseType.Post(name="Strength")
        self.assertIsNotNone(ex.id)

    def test_posting_ExerciseType_twice_returns_the_same_object(self):
        ex = ExerciseType.Post(name="Strength")
        ex2 = ExerciseType.Post(name="Strength")
        self.assertEqual(ex.id, ex2.id)

    def test_ExerciseTypes_are_unique(self):
        name = "Strength"
        ExerciseType.Post(name=name)
        ExerciseType.Post(name=name)
        count = ExerciseType.Count(name=name)
        self.assertEqual(count, 1)

    def test_ExerciseType_NullObject_method_returns_uninitialized_object(self):
        ex = ExerciseType.NullObject()
        self.assertIsNotNone(ex)
        self.assertIsNone(ex.id)
        self.assertIsNone(ex.name)

    def test_ExerciseType_GetByName_method_returns_correct_object(self):
        exName = "Plyometrics"
        ex = ExerciseType.Post(exName)
        ex2 = ExerciseType.GetByName(exName)
        self.assertIsNotNone(ex.id)
        self.assertEqual(ex.id, ex2.id)

if __name__ == "__main__":
    unittest.main()
    from Tables import _Database, _dbEngine
    _Database.drop(_dbEngine)
