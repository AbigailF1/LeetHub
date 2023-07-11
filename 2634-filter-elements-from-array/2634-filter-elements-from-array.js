/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const new_arr = new Array(arr.length)
    for(let i = 0; i < arr.length; i++){
        new_arr[i] = fn(arr[i], i)
    }
    const ans = []
    for(let i = 0; i < arr.length; i++){
        if (new_arr[i] != false){
            ans.push(arr[i])
        }
    }
    // console.log(new_arr)
    return ans
    
};