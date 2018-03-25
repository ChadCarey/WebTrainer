import unittest
import requests
from Utils.StatusCodes import *
from multiprocessing import Process
from Run import RunServer
import time

TEST_URL = "http://127.0.0.1:5000"


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.serverProcess = Process(target=RunServer, args=[])
        self.serverProcess.start()
        time.sleep(0.1)

    def test_post_exercise_type(self):
        payload = {'name' : 'something'}
        r = requests.post('/'.join([TEST_URL, 'workout_type']), data=payload)
        self.assertTrue(r.status_code == SUCCESS_STATUS)
        print r.text

    @classmethod
    def tearDownClass(self):
        self.serverProcess.terminate()
        self.serverProcess.join()


if __name__ == "__main__":
    unittest.main()
