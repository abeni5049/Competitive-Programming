class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort(key=self.compare)
        return letter_logs + digit_logs
    def compare(self, log):
        words = log.split()
        return (words[1:],words[0])
