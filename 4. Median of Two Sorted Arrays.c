double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int size= nums1Size+nums2Size;
    int a[size],i=0,j=0;
    while(i<nums1Size)
    {
        a[j]=nums1[i];
        j++;
        i++;
    }
    i=0;
    while(i<nums2Size)
    {
        a[j]=nums2[i];
        j++;
        i++;
    }

    for (int m = 0; m < j - 1; m++) {          
        for (int n = 0; n < j - m - 1; n++) {  
            if (a[n] > a[n + 1]) {          
                int temp = a[n];
                a[n] = a[n + 1];
                a[n + 1] = temp;
            }
        }
    }

    if (j%2==1) {
        return a[j/2];
    } else {
        
        return (a[j/2-1]+a[j/2])/2.0;
    }
    
}
