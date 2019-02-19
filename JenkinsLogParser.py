import re
from Helper import *


class JenkinsLogParser:

    def __init__(self, filepath):
        self.filepath = filepath
        self.lines = read_file_line_by_line(self.filepath)
        self.failed_tc = []
        self.passed_tc = []

    def get_tc(self, failed=True, include_suite=False):
        if failed:
            if len(self.failed_tc) > 0:
                print("List for failed TCs is already inited")
                return self.failed_tc
            else:
                pattern = "✗ (.*)\["
                self.failed_tc = self.get_tc_helper(pattern, include_suite)
                return self.failed_tc
        else:
            if len(self.passed_tc) > 0:
                print("List for passed TCs is already inited")
                return self.passed_tc
            else:
                pattern = "✓ (.*)\["
                self.passed_tc = self.get_tc_helper(pattern, include_suite)
                return self.passed_tc

    def get_tc_helper(self, pattern, include_suite=False):
        tcs = []
        for i, line in enumerate(self.lines):
            result = re.search(pattern, line)
            if result is not None:
                s = result.group(1)
                # s = s.replace("\t", "")
                # s = s.replace("  ", "")
                failed_tc = re.sub('[^a-zA-Z +]', '', s)
                if include_suite:
                    suite = self.get_suite(i)
                    tcs.append({suite: failed_tc})
                else:
                    tcs.append(failed_tc)
        return tcs

    def get_suite(self, line_number):
        pattern = "wavefront (.*) suite"
        for i in range(line_number, 0, -1):
            result = re.search(pattern, self.lines[i])
            if result is not None:
                return result.group(1)
        return None
