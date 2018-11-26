Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
    0(n)    

2. What is the space complexity of your `depth_first_for_each` function?
    0(n)? 

3. What is the runtime complexity of your `breadth_first_for_each` method?
4. What is the space complexity of your `breadth_first_for_each` method?
5. What is the runtime complexity of your `heapsort` function?
  0(log(n))

6. What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data. What would be the space complexity if your function instead altered the input array?
    since were returning an array of data, the space complexity is going to be 0(n).


<!-- https://cs.stackexchange.com/questions/6901/what-is-the-time-complexity-of-the-following-program/6904 -->
<!-- https://stackoverflow.com/questions/22468027/what-is-the-time-complexity-for-the-following-program -->

<!-- The time complexity here is proportional to the depth of the recursion tree. At each level, the square root of n is taken. So how many times can the square root be taken before we get 2? -->

<!-- In computer science, the time complexity is the computational complexity that describes the amount of time it takes to run an algorithm. ... Therefore, the time complexity is commonly expressed using big O notation, typically etc., where n is the input size in units of bits needed to represent the input. -->

<!-- The i for loop is of time complexity O(n), because it performs one iteration for every element of the array. For every element in the array, you are looping through it once more -- half on average in the k for loop, and half on average in the j for loop. Each of these is O(n) as well. If there are 4 elements in the array, the number of operations is proportional to n*(n - 1), but in time-complexity, constants such as the 1 are ignored. -->

<!-- The number of operations your method will perform is proportional to the number of elements in it multiplied by itself, therefore, overall, the method is O(n2). -->

<!-- Space complexity is a measure of the amount of working storage an algorithm needs. That means how much memory, in the worst case, is needed at any point in the algorithm. As with time complexity, we're mostly concerned with how the space needs grow, in big-Oh terms, as the size N of the input problem grows. -->