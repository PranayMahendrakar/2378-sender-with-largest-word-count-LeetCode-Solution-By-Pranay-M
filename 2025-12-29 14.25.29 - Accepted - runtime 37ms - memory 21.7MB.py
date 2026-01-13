class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        word_count = {}
        for message, sender in zip(messages, senders):
            count = len(message.split())
            word_count[sender] = word_count.get(sender, 0) + count
        
        max_count = max(word_count.values())
        result = ""
        for sender, count in word_count.items():
            if count == max_count and sender > result:
                result = sender
        return result