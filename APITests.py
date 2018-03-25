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
        payload = {'name': 'yoga'}
        postResult = requests.post(self.WORKOUT_TYPE_URL, data=payload)
        self.assertTrue(postResult.status_code == SUCCESS_STATUS)
        getResult = requests.get(self.WORKOUT_TYPE_URL)
        self.assertTrue(getResult.status_code == SUCCESS_STATUS)
        jsonData = json.loads(getResult.text)
        self.assertTrue(False)

    @classmethod
    def tearDownClass(self):
        self.serverProcess.terminate()
        self.serverProcess.join()


if __name__ == "__main__":
    unittest.main()
