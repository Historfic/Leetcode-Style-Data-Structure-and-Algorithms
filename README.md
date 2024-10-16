# Leetcode-Style Data Structure and Algorithms
This repository contains implementations and explanations of common data structures and algorithmic paradigms used in solving Leetcode-style problems. It covers essential topics, problem-solving strategies, and common patterns that will help in mastering coding challenges.

## 1. Common Data Structures
1.1 Arrays
Concept: Contiguous blocks of memory that store elements of the same type.
Operations: Access, insert, delete.
Common Problems:

Two Pointers Technique: (e.g., find pairs in sorted array).
Sliding Window Technique: (e.g., find the maximum sum subarray of size k).
Prefix Sum: (e.g., find a subarray that sums to a specific value).
1.2 Linked Lists
Concept: A linear collection of data elements where each element points to the next.
Operations: Traversal, insertion, deletion.
Types: Singly linked, doubly linked, circular linked list.
Common Problems:

Detect cycles.
Reverse a linked list.
Merge two sorted linked lists.
1.3 Stacks
Concept: Follows Last-In-First-Out (LIFO) principle.
Operations: Push, pop, top, isEmpty.
Common Problems:

Balanced parentheses.
Next greater element.
Implement a queue using two stacks.
1.4 Queues
Concept: Follows First-In-First-Out (FIFO) principle.
Operations: Enqueue, dequeue, front, isEmpty.
Types: Circular queue, deque (double-ended queue).
Common Problems:

Sliding window maximum.
Implement stack using queues.
1.5 Hash Maps / Hash Sets
Concept: A key-value pair data structure, allowing for constant-time lookups.
Common Problems:

Find if a pair exists with a specific sum.
Longest substring without repeating characters.
Group anagrams.
1.6 Trees
Concept: Hierarchical data structure consisting of nodes connected by edges.
Types: Binary Tree, Binary Search Tree, AVL Tree, Red-Black Tree.
Traversals: In-order, Pre-order, Post-order, Level-order.
Common Problems:

Validate binary search tree.
Lowest common ancestor.
Serialize and deserialize a binary tree.
1.7 Heaps / Priority Queues
Concept: A complete binary tree where each node is greater (max-heap) or smaller (min-heap) than its children.
Common Problems:

Find the Kth largest element.
Merge k sorted lists.
Sliding window median.
1.8 Graphs
Concept: Collection of nodes connected by edges. Can be directed/undirected, weighted/unweighted.
Common Problems:

Breadth-First Search (BFS) and Depth-First Search (DFS).
Shortest path algorithms (Dijkstra, Bellman-Ford).
Detecting cycles (using DFS).
Topological sorting.
## 2. Algorithmic Paradigms
2.1 Brute Force
Concept: Try every possible solution. Simple but inefficient.
When to Use: Small input sizes or when no better approach is available.
Example Problems:

Generate all subsets of a set.
2.2 Greedy Algorithms
Concept: Make the locally optimal choice at each step, hoping to find the global optimum.
When to Use: Problems with the greedy-choice property and optimal substructure.
Common Problems:

Activity selection.
Huffman coding.
Fractional knapsack.
2.3 Divide and Conquer
Concept: Break down the problem into smaller sub-problems, solve them independently, and combine the results.
When to Use: Recursive problems where splitting the input helps reduce complexity.
Common Problems:

Merge sort.
Quick sort.
Binary search.
2.4 Dynamic Programming (DP)
Concept: Solves problems by breaking them into overlapping subproblems, storing the results of solved subproblems to avoid recomputation.
When to Use: Problems with optimal substructure and overlapping subproblems.
Common Problems:

Fibonacci sequence.
Longest common subsequence.
Knapsack problem.
2.5 Backtracking
Concept: Try to build a solution incrementally, backtracking when a partial solution fails to satisfy the problem’s constraints.
When to Use: Problems involving choices, permutations, or combinations.
Common Problems:

N-Queens problem.
Sudoku solver.
Subset sum.
2.6 Binary Search
Concept: Efficient algorithm for finding the position of a target element in a sorted array.
When to Use: When the problem involves searching in a sorted list.
Common Problems:

Find an element in a rotated sorted array.
Search in a 2D matrix.
Find the peak element.
## 3. Problem-Solving Strategies
3.1 Clarify the Problem
Understand the input format, constraints, and desired output.
Ask questions to clarify ambiguous conditions.
Identify edge cases like empty inputs, very large inputs, or inputs with duplicates.
3.2 Choose the Right Data Structure
Based on the problem, decide which data structure offers the best time complexity.
For example, if you need fast lookups, a hash map is often the best choice.
3.3 Optimize Time and Space Complexity
Focus on finding solutions that have efficient time complexity, ideally O(log n), O(n), or O(n log n).
Be mindful of memory usage, particularly for recursive solutions that could overflow the call stack.
3.4 Dry Run the Algorithm
Walk through your solution with small sample inputs to ensure correctness before implementing.
Ensure edge cases are handled, such as empty inputs, repeated elements, and large datasets.
## 4. Common Leetcode Problem Patterns
4.1 Two Pointers
Used in problems involving arrays or linked lists, where two pointers traverse the data structure from opposite ends or in different ways.
Example Problems: Pair Sum, Container with Most Water, Remove Duplicates.

4.2 Sliding Window
Helps to solve problems that require finding the optimal range or subarray.
Example Problems: Maximum sum of subarray of size k, Longest substring with at most k distinct characters.

4.3 Binary Search on Answer
A specialized form of binary search where the solution space (the possible values) is searched instead of the input array itself.
Example Problems: Find the minimum capacity required to ship packages within D days.

4.4 Topological Sorting
Used for problems involving dependency graphs, where you need to determine a valid order of tasks.
Example Problems: Course schedule, Task scheduling.

## 5. Practice Tips
Start Simple: Focus on mastering easy problems before moving to harder ones.
Focus on Patterns: Try to recognize the underlying pattern of a problem (e.g., greedy, sliding window, dynamic programming).
Time Yourself: Leetcode problems are often timed during interviews. Practice under time constraints.
Analyze Solutions: After solving a problem, review the optimal solution, even if you got it correct. This helps you improve and learn new techniques.
Optimize Code: Try to write clean, readable, and optimized code that balances both time and space complexity.
By practicing these techniques and understanding the theory behind each approach, you’ll become proficient in solving Leetcode-style problems.