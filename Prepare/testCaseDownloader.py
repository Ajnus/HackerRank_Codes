import requests

TESTCASESFOLDER = "Prepare/Algorithms/Warmup/Mini-Max Sum/test cases"    # insert yours

# INPUT AND OUTPUT URL'S OF GIVEN TESTCASE
URL_ARRAY=["https://hr-testcases-us-east-1.s3.amazonaws.com/26276/input14.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240217%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240217T003857Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=65444c85db29d25f4315cc04281a885b891a7db87a3cc7d708ea10dcf59dee76",
           "https://hr-testcases-us-east-1.s3.amazonaws.com/26276/output14.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240217%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240217T003928Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=2d315bdecd80216c62153a61c3ad7344d6589ac74f149f3a7abe4f62b088d849"]

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