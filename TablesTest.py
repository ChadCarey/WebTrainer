import unittest
import Database
from Database.ExerciseType import ExerciseType
import json

class TestExerciseTypesTable(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        Database.Initialize()

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

    def test_ExerciseType_Get_method_returns_a_list_of_all_ExerciseTypes(self):
        # generate a list of workouts to add
        exerciseNames = ["cardio_"+str(x) for x in xrange(0,10)]
        for exerciseName in exerciseNames:
            id = ExerciseType.Post(exerciseName).id

        exerciseList = ExerciseType.GetAll()
        self.assertGreaterEqual(len(exerciseList), len(exerciseNames))

        # contains at least the exercises we just added
        addedExerciseNames = [ex.name for ex in exerciseList]
        print addedExerciseNames
        for exerciseName in exerciseNames:
            print exerciseName
            self.assertTrue(exerciseName in addedExerciseNames)

    def test_ExerciseType_json_property_returns_json_str(self):
        exName = "Plyometrics"
        ex = ExerciseType.Post(exName)
        self.assertTrue(type(ex.json) == str)

    def test_ExerciseType_json_contains_an_id_and_correct_name(self):
        exName = "Plyometrics"
        ex = ExerciseType.Post(exName)
        jsonData = json.loads(ex.json)
        self.assertIsNotNone(jsonData['id'])
        self.assertTrue(jsonData['name'] == exName.lower())


if __name__ == "__main__":
    unittest.main()
    from Tables import _Database, _dbEngine
    # cleanup
    _Database.drop(_dbEngine)
