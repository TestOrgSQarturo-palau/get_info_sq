import json
import os

# Function to parse a json file and extract the values of the parameters            
def parse_json_file(file_path, parameters):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        result = {}
        for parameter in parameters:
            parts = parameter.split('.')
            value = data
            for part in parts:
                if isinstance(value, dict):
                    value = value.get(part)
                else:
                    value = None
                    break
            result[parameter] = value
        return result

def get_json_files_in_directory():
    directory = os.path.dirname(os.path.abspath(__file__))
    json_files = []
                
    for file in os.listdir(directory):
        if file.endswith(".json"):
            json_files.append(file)
    
    return json_files


# Get the list of json files in the current directory
json_files = get_json_files_in_directory()
print(json_files)

# Filter to get only the sonarqube-support-info files (there should be only one)           
for file in json_files:
    if file.startswith("sonarqube-support-info"):
        file_path = file
        parameters = ["System.Server ID", 
                      "System.Version",
                      "License.type",
                      "ALMs",
                      "Server Push Connections.SonarLint Connected Clients",
                      "statistics.userCount",
                      "statistics.projectCount",
                      "statistics.nclocByLanguage",
                      "Database"]
        result = parse_json_file(file_path, parameters)
        print(result)
        



