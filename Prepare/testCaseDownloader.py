import requests

TESTCASESFOLDER = "Prepare/Algorithms/Warmup/Mini-Max Sum/test cases"    # insert yours

# INPUT AND OUTPUT URL'S OF GIVEN TESTCASE
URL_ARRAY=["https://hr-testcases-us-east-1.s3.amazonaws.com/26276/input09.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240213%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240213T160455Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=b380a98b569ce0688800f7247778628876d5b15c1b8c22cee6ac5092ed9c842f",
           "https://hr-testcases-us-east-1.s3.amazonaws.com/26276/output09.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240213%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240213T160457Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=29c050dce7daf3247f75a1ea8e7607684db3b5fc7724ed02328bafaaf31d157e"]

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