from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid_ips = []

        def is_valid(segment):
            # A valid segment should be non-empty and not start with '0' if its length is greater than 1
            return len(segment) == 1 or (segment[0] != '0' and 0 <= int(segment) <= 255)

        def backtrack(index, curr_ip):
            if index == len(s) and len(curr_ip) == 4:
                valid_ips.append('.'.join(curr_ip))
                return

            if len(curr_ip) >= 4:
                return

            for i in range(index, min(index + 3, len(s))):
                segment = s[index:i + 1]
                if is_valid(segment):
                    curr_ip.append(segment)
                    backtrack(i + 1, curr_ip)
                    curr_ip.pop()

        backtrack(0, [])
        return valid_ips