class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = {}

        for word in strs:
            key = ' '.join(sorted(word))
            if key not in bucket:
                bucket[key] = []
            bucket[key].append(word)

        return list(bucket.values())        


        