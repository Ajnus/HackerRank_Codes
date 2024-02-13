import requests

TESTCASESFOLDER = "Prepare/Algorithms/Warmup/Plus Minus/test cases"    # insert yours
URL = "https://hr-testcases-us-east-1.s3.amazonaws.com/8654/output10.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20240213%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240213T020623Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=753785fc2346a3c0be524743dfa0808cc3c57aff2fda750ec365e9dc1431966d"
                                                                                # insert yours

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