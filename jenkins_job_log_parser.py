#!/usr/bin/env python3
import sys
from JenkinsLogParser import JenkinsLogParser
from Helper import *

log_file = sys.argv[1]

jlp = JenkinsLogParser(log_file)
failed = jlp.get_tc(failed=True, include_suite=True)
passed = jlp.get_tc(failed=False, include_suite=True)

real_fail = []
for f in failed:
    if f not in passed:
        real_fail.append(f)

# print(real_fail)
ll = remove_duplicates_from_dict_list(real_fail)

for l in ll:
    print(l)
