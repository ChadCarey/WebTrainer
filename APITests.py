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
        self.serverProcess = Process(target=RunServer, args=[])
        self.serverProcess.start()
        time.sleep(0.1)

    def test_post_exercise_type(self):
        payload = {'name': 'yoga'}
        r = requests.post('/'.join([TEST_URL, 'workout_type']), data=payload)
        self.assertTrue(r.status_code == SUCCESS_STATUS)
        jsonData = json.loads(r.text)
        self.assertTrue(jsonData['name'] == payload['name'])
        self.assertTrue(jsonData['data_type'] == 'ExerciseType')
        self.assertIsNotNone(jsonData['id'])

    @classmethod
    def tearDownClass(self):
        self.serverProcess.terminate()
        self.serverProcess.join()


if __name__ == "__main__":
    unittest.main()
