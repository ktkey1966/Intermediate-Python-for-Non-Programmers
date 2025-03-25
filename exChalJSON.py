#Inside the get_scores function, return a list of all the 
# student's scores on their first test.

show_expected_result = False

import json

# Properly formatted JSON string
thestr = """
{
    "students": [
        {
            "name": "Nick",
            "scores": [
                56,
                73,
                68,
                84
            ]
        },
        {
            "name": "Jane",
            "scores": [
                88,
                74,
                91,
                73
            ]
        },
        {
            "name": "Mark",
            "scores": [
                93,
                66,
                52,
                33
            ]
        }
    ]
}
"""

# Parse the JSON string
json_course_data = json.loads(thestr)

# Function to extract the first test scores
def get_scores():
    first_test_scores = []
    for student in json_course_data["students"]:
        first_test_scores.append(student["scores"][0])  # Get the first score
    return first_test_scores

# Run the function and print the result
print(get_scores())