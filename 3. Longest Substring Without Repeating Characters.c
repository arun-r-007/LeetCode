#include<string.h>
#include<stdlib.h>


int lengthOfLongestSubstring(char *s) {
    int n = strlen(s);
    int maxLength = 0;
    int i = 0, j = 0;
    int charIndex[128] = {0};  
    while (j < n) {
        char currentChar = s[j];
        
        
        if (charIndex[currentChar] > i) {
            i = charIndex[currentChar];
        }
        
        
        int currentLength = j - i + 1;
        if (currentLength > maxLength) {
            maxLength = currentLength;
        }

     
        charIndex[currentChar] = j + 1;
        
       
        j++;
    }

    return maxLength;
}