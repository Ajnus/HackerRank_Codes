import requests

TESTCASESFOLDER = "Prepare/Algorithms/Warmup/Staircase/test cases"    # insert yours

# INPUT AND OUTPUT URL'S OF GIVEN TESTCASE
URL_ARRAY=["https://hr-testcases-us-east-1.s3.amazonaws.com/8636/input08.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240213%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240213T151558Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=404d7e0743e725340c467bd3c698bee0a8f62412de4922e8f1f8a8b97f3cb664",
           "https://hr-testcases-us-east-1.s3.amazonaws.com/8636/output08.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240213%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240213T151617Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=722ee77f45b7c6444a5e5591ae7fe18036a3b0e6bb6570f16f580d8806e48640"]

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