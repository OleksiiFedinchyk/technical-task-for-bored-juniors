import requests
from pytest import raises
from wrapper import Wrapper


def test_wrapper_queries_dict():
    wrapper = Wrapper("education", "1", "0.1", "30", "0.1", "0.5")
    assert wrapper.queries_dict == {"type": "education",
                             "participants": "1",
                             "minprice": "0.1",
                             "maxprice": "30",
                             "minaccessibility": "0.1",
                             "maxaccessibility": "0.5"}

def test_get_activity_with_command_line_arguments():
    wrapper = Wrapper("education", "1", "0.1", "30", "0.1", "0.5")
    assert wrapper.get_activity() == "http://www.boredapi.com/api/activity?type=education&participants=1&minprice=0.1&maxprice=30&minaccessibility=0.1&maxaccessibility=0.5"

def test_get_activity_without_command_line_arguments():
    wrapper = Wrapper()
    assert wrapper.get_activity() == "http://www.boredapi.com/api/activity/"

""" To check this out I use the value 10 for participants and this get request will respond
{
  "error": "No activity found with the specified parameters"
}
    And when tries to get value from activity-key, the program will raise KeyError
"""
def test_access_activity_value():
    with raises(KeyError):
        wrapper = Wrapper("education", "10", "0.1", "30", "0.1", "0.5")
        activity = requests.get(wrapper.get_activity()).json()["activity"]




