/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {

    if (!arr.length || size <= 0)
    {
        return [];
    }

    const split_array = [];
    const n = arr.length;

    for (let i = 0 ;i < n; i += size)
    {
        const slice1 = arr.slice(i, i + size);
        split_array.push(slice1);
    }

    return split_array;
    
};
