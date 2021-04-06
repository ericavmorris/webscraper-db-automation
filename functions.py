import shutil, os, sys, fnmatch
import pdb
from company_name_mapping import company_mappings


def is_db_in_folder(downloaded_csv_path, expected_destination_folder_path):

    present_csv_file = find_file('*.csv', expected_destination_folder_path)

    if present_csv_file == False:
        return False
    else:
        return True




def find_file(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))

    if len(result) > 0:
        return result[0]
    else:
        return False

def create_company_directory(company_name):
    if not os.path.exists(company_mappings[company_name]):
        os.makedirs(company_mappings[company_name])


# is_db_in_folder("/Users/camillefeghali/dev/frontend-master/automation/covid-automation/COVID-19_Dashboard_Input_-_March_2020_Data-2020-05-07_13-08-18.csv", "/Users/camillefeghali/dev/frontend-master/automation/covid-automation/AccurateGroup/")