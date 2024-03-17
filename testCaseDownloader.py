import requests

PROBLEM = "Organizing Containers of Balls"                                       # custom
TESTCASESFOLDER = f"Prepare/Algorithms/Implementation/{PROBLEM}/test cases"     # insert yours

# INPUT AND OUTPUT URL'S OF GIVEN TESTCASE
URL_ARRAY=["https://hr-testcases-us-east-1.s3.amazonaws.com/32644/input05.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240317%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240317T034247Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=b18f50624af81bf8dafdb4add4a9cc14b5cdb939ae2174a3eca5fd2648f2e570",
           "https://hr-testcases-us-east-1.s3.amazonaws.com/32644/output05.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240317%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240317T034224Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=5f47b8f1231a1e0bedef0311de764964e201f437bd289ded304216d53295b084"]

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