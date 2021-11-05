// Please write a class in the language of your choice that contains the following two public methods:
// 1.	aboveBelow
// •	accepts two arguments
// o	a collection of integers (the list)
// o	an integer (the comparison value)
// •	returns a hash/object/map/etc. with the keys "above" and "below" with the corresponding count of integers from the list that are above or below the comparison value
// Example usage:
// input: [1,2,3,4,5,6], 3
// output: { "above": 3, "below": 2 }
// 1.	stringRotation
// •	accepts two arguments
// o	a string (the original string)
// o	a positive integer (the rotation amount)
// •	returns a new string, rotating the characters in the original string to the right by the rotation amount and have the overflow appear at the beginning
// Example usage:
// input: "MyString", 2
// output: "ngMyStri"
// Let us know if you have any questions! If you're good to go, please send us back your exercise at your convenience (please upload your response to a public git repository, such as Github).

class Transform {

    aboveBelow(numArr, int) {
        let res = new Object();
        let indx = numArr.indexOf(int)
        if (indx === -1) {
            return "Integer not found"
        } else {
            res.above = (numArr.length - 1) - indx
            res.below = indx
            return res
        }
    }

    stringRotation(str, num) {
        if (num > str.length) {
            return `Enter a number less than ${str.length}`
        }
        let strArr = str.split('')
        let res = new Array()

        for (let i = str.length - num; i < strArr.length; i++) {
            let char = strArr[i]
            res.push(char)
        }
        strArr.splice(str.length - num)
        return [...res, ...strArr].join('')
    }

}

const obj = new Transform()
// console.log(obj.aboveBelow([3, 1, 4, 8, 2, 9], 3))
// console.log(obj.aboveBelow([1, 2, 3, 4, 5, 6], 3))
// console.log(obj.aboveBelow([1, 2, 3, 4, 5, 6], 1))
// console.log(obj.aboveBelow([1, 2, 3, 4, 5, 6], 6))
// console.log(obj.aboveBelow([1, 2, 3, 4, 5, 6], -1))
// console.log(obj.stringRotation("MyString", 0))
// console.log(obj.stringRotation("MyString", 1))
// console.log(obj.stringRotation("MyString", 2))
// console.log(obj.stringRotation("MyString", 3))
// console.log(obj.stringRotation("MyString", 4))
// console.log(obj.stringRotation("MyString", 5))
// console.log(obj.stringRotation("MyString", 6))
// console.log(obj.stringRotation("MyString", 7))
// console.log(obj.stringRotation("MyString", 30))
