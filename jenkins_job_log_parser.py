#!/usr/bin/env python
import re

def get_failed_passed_tc(file_name):
    failed_tc = []
    passed_tc = []
    with open(file_name, encoding="utf-8") as f:
        lines = f.readlines()
# ✓
    for line in lines:
        result = re.search("✗ (.*)\[", line)
        if result is not None:
            s = result.group(1)
            # s = s.replace("\t", "")
            # s = s.replace("  ", "")
            failed_tc.append(re.sub('[^a-zA-Z +]', '', s))

    for line in lines:
        result = re.search("✓ (.*)\[", line)
        if result is not None:
            s = result.group(1)
            # s = s.replace("\t", "")
            # s = s.replace("  ", "")
            passed_tc.append(re.sub('[^a-zA-Z +]', '', s))

    return list(set(failed_tc)), list(set(passed_tc))


master = "e2e_master"
rbac = "e2e_rbac_flag_on"

failed_test_cases_in_master, passed_test_cases_in_master = get_failed_passed_tc(master)
failed_test_cases_in_rbac, passed_test_cases_in_rbac = get_failed_passed_tc(rbac)

print("failed test cases count in master: ", len(failed_test_cases_in_master))
print("failed test cases count in rbac: ", len(failed_test_cases_in_rbac))

failed_in_both = []

failed_in_master = []
filed_in_rbac = []

for tc in failed_test_cases_in_rbac:
    if tc not in passed_test_cases_in_rbac:
        filed_in_rbac.append(tc)

# for tc in failed_test_cases_in_master:
#     if tc not in passed_test_cases_in_master:
#         failed_in_master.append(tc)

for tc in failed_test_cases_in_rbac:
    if tc in failed_test_cases_in_master:
        failed_in_both.append(tc)

print("failed test cases in both: ", len(failed_in_both), "\n\n\n")

print("*****Failed test cases only in rbac*****")
for tc in failed_test_cases_in_rbac:
    if tc not in failed_in_both:
        print(tc)

print("\n\n\n*****Failed test cases only in master*****")
for tc in failed_test_cases_in_master:
    if tc not in failed_in_both:
        print(tc)
