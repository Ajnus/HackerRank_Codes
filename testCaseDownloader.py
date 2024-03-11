import requests

PROBLEM = "Picking Numbers"                                       # custom
TESTCASESFOLDER = f"Prepare/Algorithms/Implementation/{PROBLEM}/test cases"     # insert yours

# INPUT AND OUTPUT URL'S OF GIVEN TESTCASE
URL_ARRAY=["https://hr-testcases-us-east-1.s3.amazonaws.com/29526/input09.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240311%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240311T030854Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=0dfe584cbf555a19757caf23acbc662fdbf2e62259c44c4e9b906c8796ae2532",
           "https://hr-testcases-us-east-1.s3.amazonaws.com/29526/output09.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240311%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240311T030859Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=7fc0039d6021cbcc793add02d05708d7a00e7ed34cd58d85b2b9153f87d4dbd1"]

print(f"----------------------\n{PROBLEM}: ")

for url in URL_ARRAY:

    URL = url

    # MAKE USE OF THE URL TO CREATE FILES WITH HACKERRANK'S FOLDER STRUCTURE
    number_index = next((i for i, c in enumerate(URL[53:]) if c.isdigit()), None)
    mode = URL[53:53 + number_index]                                                # 'input/output'
    case_number = URL[53 + number_index:53 + number_index + 2]                      # 'XX' right after
    FILEPATH = f"{TESTCASESFOLDER}/{mode}/{mode}{case_number}.txt"

    # GET THE DATA FROM URL
    r = requests.get(URL)

    # SAVE IT IN LOCAL FILE
    with open(FILEPATH, 'wb') as f:
        f.write(r.content)
    print(f"{mode}{case_number} done")

print("----------------------")