import unittest
import main
import hug


class FlappingScenariosTests(unittest.TestCase):
    def test_connection(self):
        result = hug.test.get(main, '/flapping_scenarios')
        self.assertEqual(result.status, hug.HTTP_200, "Should be ok")

    def test_does_one_is_added_when_one(self):
        json_object = [{"service_id": 1, "duration": 15, "startTime": "2020-07-02  09:01:31"}]
        result_to_test = main.detect_flapping_scenarios(json_object)
        self.assertEqual(len(result_to_test), 1, "The flapping scenarios should be 1")

    def test_does_one_is_added_when_multiple(self):
        json_object = [{"service_id": 1, "duration": 2, "startTime": "2020-07-02  09:01:31"},
                       {"service_id": 1, "duration": 3, "startTime": "2020-07-02  09:11:31"},
                       {"service_id": 1, "duration": 2, "startTime": "2020-07-02  09:51:31"},
                       {"service_id": 1, "duration": 9, "startTime": "2020-07-02  08:30:31"}
                       ]
        result_to_test = main.detect_flapping_scenarios(json_object)
        self.assertEqual(len(result_to_test), 1, "The flapping scenarios should be 1")

    def test_does_multiple_are_added(self):
        json_object = [{"service_id": 1, "duration": 2, "startTime": "2020-07-02 09:01:31"},
                       {"service_id": 1, "duration": 3, "startTime": "2020-07-02 09:11:31"},
                       {"service_id": 1, "duration": 5, "startTime": "2020-07-02 09:51:31"},
                       {"service_id": 1, "duration": 2, "startTime": "2020-07-02 10:30:31"},
                       {"service_id": 1, "duration": 5, "startTime": "2020-07-02 10:40:31"},
                       {"service_id": 1, "duration": 3, "startTime": "2020-07-02 10:50:31"}
                       ]
        result_to_test = main.detect_flapping_scenarios(json_object)
        self.assertEqual(len(result_to_test), 3, "The flapping scenarios should be 1")

    def test_does_outages_sum_is_correct(self):
        json_object = [{"service_id": 1, "duration": 2, "startTime": "2020-07-02 09:01:31"},
                       {"service_id": 1, "duration": 3, "startTime": "2020-07-02 09:11:31"},
                       {"service_id": 1, "duration": 2, "startTime": "2020-07-02 09:51:31"},
                       {"service_id": 1, "duration": 9, "startTime": "2020-07-02 08:30:31"}
                       ]
        result_to_test = main.detect_flapping_scenarios(json_object)
        self.assertEqual(result_to_test[0]['sumOfOutages'], 16, "The sum of outages should be 16")

    def test_does_amount_of_outages_is_correct(self):
        json_object = [{"service_id": 1, "duration": 2, "startTime": "2020-07-02 09:01:31"},
                       {"service_id": 1, "duration": 3, "startTime": "2020-07-02 09:11:31"},
                       {"service_id": 1, "duration": 2, "startTime": "2020-07-02 09:51:31"},
                       {"service_id": 1, "duration": 9, "startTime": "2020-07-02 08:30:31"}
                       ]
        result_to_test = main.detect_flapping_scenarios(json_object)
        self.assertEqual(result_to_test[0]['amountOfOutages'], 4, "The amount of outages should be 4")

    def test_does_endTime_is_correct(self):
        json_object = [{"service_id": 1, "duration": 2, "startTime": "2020-07-02 09:01:31"},
                       {"service_id": 1, "duration": 3, "startTime": "2020-07-02 09:11:31"},
                       {"service_id": 1, "duration": 2, "startTime": "2020-07-02 09:51:31"},
                       {"service_id": 1, "duration": 9, "startTime": "2020-07-02 08:30:31"}
                       ]
        result_to_test = main.detect_flapping_scenarios(json_object)
        self.assertEqual(result_to_test[0]['endTime'], "2020-07-02 09:53:31",
                         "The end time should be 2020-07-02 09:53:31")

    def test_does_added_correctly_when_part_of_duration_is_out_of_timeframe(self):
        json_object = [{"service_id": 1, "duration": 5, "startTime": "2020-07-02 09:01:31"},
                       {"service_id": 1, "duration": 1, "startTime": "2020-07-02 09:11:31"},
                       {"service_id": 1, "duration": 1, "startTime": "2020-07-02 09:51:31"},
                       {"service_id": 1, "duration": 1, "startTime": "2020-07-02 10:30:31"},
                       {"service_id": 1, "duration": 1, "startTime": "2020-07-02 10:40:31"},
                       {"service_id": 1, "duration": 10, "startTime": "2020-07-02 10:54:31"}
                       ]
        result_to_test = main.detect_flapping_scenarios(json_object)
        self.assertEqual(len(result_to_test), 1, "The flapping scenarios should be 1")

    def test_does_endTime_is_correct_when_part_of_duration_is_out_of_timeframe(self):
        json_object = [{"service_id": 1, "duration": 5, "startTime": "2020-07-02 09:01:31"},
                       {"service_id": 1, "duration": 1, "startTime": "2020-07-02 09:11:31"},
                       {"service_id": 1, "duration": 1, "startTime": "2020-07-02 09:51:31"},
                       {"service_id": 1, "duration": 1, "startTime": "2020-07-02 10:30:31"},
                       {"service_id": 1, "duration": 1, "startTime": "2020-07-02 10:40:31"},
                       {"service_id": 1, "duration": 10, "startTime": "2020-07-02 10:54:31"}
                       ]
        result_to_test = main.detect_flapping_scenarios(json_object)
        self.assertEqual(result_to_test[0]['endTime'], "2020-07-02 11:01:31",
                         "The end time should be 2020-07-02 11:01:31")

    def test_does_work_correctly_with_multiple_services(self):
        json_object = [{"service_id": 1, "duration": 8, "startTime": "2020-07-02 10:40:31"},
                       {"service_id": 1, "duration": 7, "startTime": "2020-07-02 10:54:30"},
                       {"service_id": 1, "duration": 2, "startTime": "2020-07-02 10:54:31"},
                       {"service_id": 2, "duration": 1, "startTime": "2020-07-02 09:11:31"},
                       {"service_id": 2, "duration": 1, "startTime": "2020-07-02 09:51:31"},
                       {"service_id": 3, "duration": 5, "startTime": "2020-07-02 09:01:31"},
                       {"service_id": 3, "duration": 1, "startTime": "2020-07-02 10:30:31"},
                       {"service_id": 5, "duration": 2, "startTime": "2020-07-02 10:53:31"},
                       {"service_id": 5, "duration": 9, "startTime": "2020-07-02 10:54:31"},
                       {"service_id": 5, "duration": 8, "startTime": "2020-07-02 10:55:31"}
                       ]
        result_to_test = main.detect_flapping_scenarios(json_object)
        self.assertEqual(len(result_to_test), 1, "Should be one")

    def test_does_sum_more_than_timeframe(self):
        json_object = [{"service_id": 1, "duration": 200, "startTime": "2020-07-02 09:01:31"},
                       ]
        result_to_test = main.detect_flapping_scenarios(json_object)
        self.assertEqual(result_to_test[0]['sumOfOutages'], 120, "The sum of outages should be 120 as maximum")

    def test_does_sum_when_outages_are_contained(self):
        json_object = [{"service_id": 1, "duration": 100, "startTime": "2020-07-02 09:01:31"},
                       {"service_id": 1, "duration": 30, "startTime": "2020-07-02 09:11:31"}
                       ]
        result_to_test = main.detect_flapping_scenarios(json_object)
        self.assertEqual(result_to_test[0]['sumOfOutages'], 100, "The sum of outages should be 100")

    def test_does_amount_is_correct(self):
        json_object = [{"service_id": 1, "duration": 2, "startTime": "2020-07-05 05:24:55"},
                       {"service_id": 1, "duration": 9, "startTime": "2020-07-05 05:32:55"}]
        result_to_test = main.detect_flapping_scenarios(json_object)
        self.assertEqual(len(result_to_test), 0, "Should be zero")

    if __name__ == '__name__':
        unittest.main()
