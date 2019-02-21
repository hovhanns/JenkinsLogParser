#!/usr/bin/env python3
import sys
from JenkinsLogParser import JenkinsLogParser
from Helper import *

log_file = sys.argv[1]

jlp = JenkinsLogParser(log_file)
failed = jlp.get_tc(failed=True, detailed=True)
passed = jlp.get_tc(failed=False, detailed=True)

# print(failed)
# print(passed)

real_fail = []
for i in range(len(failed["testCase"])):
    if failed["testCase"][i] not in passed["testCase"]:
        real_fail.append({"testCase": failed["testCase"][i],
                          "suite": failed["suite"][i],
                          "reason": failed["reason"][i]
                          })

ll = remove_duplicates_from_dict_list(real_fail)

for l in ll:
    print(l)
