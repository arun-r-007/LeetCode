def sort_by_frequency(s: str) -> str:
    #write your code here...
    
    freq = {}
    
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    result = ""

    while freq:
        
        # max_char = None

        # for ch in freq:
        #     if max_char is None:
        #         max_char = ch
        #     elif freq[ch] > freq[max_char]:
        #         max_char = ch
        #     elif freq[ch] == freq[max_char] and ch < max_char:
        #         max_char = ch
        
        max_char = max(freq, key=lambda ch: (freq[ch], -ord(ch)))
        
        result += max_char * freq[max_char]
        
        del freq[max_char]

    return result