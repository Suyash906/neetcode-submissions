class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


        prime_to_anagrams = defaultdict(list)


        for word in strs:
            key = 1
            for ch in word:
                key *= primes[ord(ch) - 97]

            prime_to_anagrams[key].append(word)

        

        return [curr for curr in prime_to_anagrams.values()]
