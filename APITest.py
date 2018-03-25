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
        print "Starting Flask server"
        self.serverProcess = Process(target=RunServer, args=[])
        self.serverProcess.start()
        time.sleep(0.1)

    def test_post_exercise_type(self):
        print "Starting test"
        r = requests.post('/'.join([TEST_URL, 'workout_type']))
        self.assertTrue(r.status_code == SUCCESS_STATUS)

    @classmethod
    def tearDownClass(self):
        print "Shutting down Flask server"
        self.serverProcess.terminate()
        self.serverProcess.join()


if __name__ == "__main__":
    unittest.main()
