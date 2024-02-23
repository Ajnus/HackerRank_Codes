import requests

PROBLEM = "Birthday Cake Candles"                                       # custom
TESTCASESFOLDER = f"Prepare/Algorithms/Warmup/{PROBLEM}/test cases"     # insert yours

# INPUT AND OUTPUT URL'S OF GIVEN TESTCASE
URL_ARRAY=["https://hr-testcases-us-east-1.s3.amazonaws.com/23074/input04.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240223%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240223T163759Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=c569f3efa8df0a661d40c0d645a4a514ffd13975dbd97768a1034c6ffbf23b85",
           "https://hr-testcases-us-east-1.s3.amazonaws.com/23074/output04.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240223%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240223T163820Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=d0d752855c2193a79ab697cc67bfeffb6218182c6d2971b815006b35aea96e06"]

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