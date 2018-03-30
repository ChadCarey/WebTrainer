import unittest
import requests
from Utils.StatusCodes import *
from multiprocessing import Process
from Run import RunServer
import time
import json

TEST_URL = "http://127.0.0.1:5000"


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # define URLs
        self.WORKOUT_TYPE_URL = '/'.join([TEST_URL, 'workout_type'])

        # kick off server
        self.serverProcess = Process(target=RunServer, args=[])
        self.serverProcess.start()
        time.sleep(0.1)

    def test_post_exercise_type(self):
        payload = {'name': 'yoga'}
        result = requests.post(self.WORKOUT_TYPE_URL, data=payload)
        self.assertTrue(result.status_code == SUCCESS_STATUS)
        jsonData = json.loads(result.text)
        self.assertTrue(jsonData['name'] == payload['name'])
        self.assertTrue(jsonData['data_type'] == 'ExerciseType')
        self.assertIsNotNone(jsonData['id'])

    def test_get_ExerciseType_returns_all_ExerciseTypes(self):
        # add the item before we try to get it
        postResult = requests.post(self.WORKOUT_TYPE_URL, data={'name': 'yoga1'})
        postResult = requests.post(self.WORKOUT_TYPE_URL, data={'name': 'yoga2'})
        postResult = requests.post(self.WORKOUT_TYPE_URL, data={'name': 'yoga3'})
        getResult = requests.get(self.WORKOUT_TYPE_URL)
        self.assertTrue(getResult.status_code == SUCCESS_STATUS)
        jsonData = json.loads(getResult.text)
        found = [x['name'] for x in jsonData if 'yoga' in x['name']]
        self.assertGreaterEqual(len(found), 3)

    def test_delete_ExerciseType_removes_ExerciseType(self):
        requests.post(self.WORKOUT_TYPE_URL, data={'name': 'yoga1'})
        allItems = json.loads(requests.get(self.WORKOUT_TYPE_URL).text)
        startingCount = len(allItems)
        for item in allItems:
            requests.delete(self.WORKOUT_TYPE_URL, data={'name': item['name']})
        allItemsAfterDelete = json.loads(requests.get(self.WORKOUT_TYPE_URL).text)
        self.assertEqual(0, len(allItemsAfterDelete))

    @classmethod
    def tearDownClass(self):
        self.serverProcess.terminate()
        self.serverProcess.join()


if __name__ == "__main__":
    unittest.main()
