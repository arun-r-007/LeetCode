#include <stdio.h>
#include <string.h>

int expandAroundCenter(char* s, int left, int right) {
    while (left >= 0 && right < strlen(s) && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1;
}

char* longestPalindrome(char* s) {
    int start = 0, end = 0;
    int len = strlen(s);

    if (len == 0) return "";

    for (int i = 0; i < len; i++) {
        int len1 = expandAroundCenter(s, i, i);
        int len2 = expandAroundCenter(s, i, i + 1);
        int maxLen = (len1 > len2) ? len1 : len2;

        if (maxLen > end - start) {
            start = i - (maxLen - 1) / 2;
            end = i + maxLen / 2;
        }
    }

    char* result = (char*)malloc(end - start + 2);
    strncpy(result, s + start, end - start + 1);
    result[end - start + 1] = '\0';
    return result;
}
