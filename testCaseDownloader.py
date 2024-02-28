import requests

PROBLEM = "Cats and a Mouse"                                       # custom
TESTCASESFOLDER = f"Prepare/Algorithms/Implementation/{PROBLEM}/test cases"     # insert yours

# INPUT AND OUTPUT URL'S OF GIVEN TESTCASE
URL_ARRAY=["https://hr-testcases-us-east-1.s3.amazonaws.com/29054/input01.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240228T023347Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=a90203f3fc63e0fd9ed5dfcb17628a817e2134a5f87c4f704964b66ecb48f430",
           "https://hr-testcases-us-east-1.s3.amazonaws.com/29054/output01.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240228T023539Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=37fc865ed67bdee054e2622aba49fcaf90a459ff3549f11fbc2fb8031dfaaebf"]

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