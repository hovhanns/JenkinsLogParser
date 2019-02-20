import re
from Helper import *


class JenkinsLogParser:

    def __init__(self, filepath):
        self.filepath = filepath
        self.lines = read_file_line_by_line(self.filepath)
        self.failed_tc = []
        self.passed_tc = []

    def get_tc(self, failed=True, detailed=False):
        if failed:
            if len(self.failed_tc) > 0:
                print("List for failed TCs is already inited")
                return self.failed_tc
            else:
                pattern = "✗ (.*)\["
                self.failed_tc = self.get_tc_helper(pattern, detailed)
                return self.failed_tc
        else:
            if len(self.passed_tc) > 0:
                print("List for passed TCs is already inited")
                return self.passed_tc
            else:
                pattern = "✓ (.*)\["
                self.passed_tc = self.get_tc_helper(pattern, detailed)
                return self.passed_tc

    def get_tc_helper(self, pattern, detailed=False):
        tcs = []
        for i, line in enumerate(self.lines):
            result = re.search(pattern, line)
            if result is not None:
                s = result.group(1)
                # s = s.replace("\t", "")
                # s = s.replace("  ", "")
                testCase = re.sub('[^a-zA-Z +]', '', s)
                if detailed:
                    suite = self.get_suite(i)
                    reason = self.get_reason(i)
                    tcs.append({"suite": suite, "testCase": testCase, "reason": reason})
                else:
                    tcs.append({"testCase": testCase})
        return tcs

    def get_suite(self, line_number):
        pattern = "wavefront (.*) suite"
        for i in range(line_number, 0, -1):
            result = re.search(pattern, self.lines[i])
            if result is not None:
                return result.group(1)
        return None

    def get_reason(self, line_number):
        pattern = '(Failed: |Expected |Error: )(.*)'
        result = re.search(pattern, self.lines[line_number + 1])
        if result is not None:
            return result.group(2).replace("\x1b", "")
        return None
