# Meta-Data-Scientist-Prep
Exercises from Meta candidate space
(All copyrights of the exercises below belong to Meta)

STRINGS

I. Rotational Cipher

One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.

For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.

Given a string and a rotation factor, return an encrypted string.

II. Matching Pairs

Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.

A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively. The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.

Note: This means you must swap two characters at different indices.

III. Minimum Length Substrings

You are given two strings s and t. You can select any substring of string s and rearrange the characters of the selected substring. Determine the minimum length of the substring of s such that string t is a substring of the selected substring.

ARRAYS

I. Reverse to Make Equal

Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.

II. Passing Yearbooks

There are n students, numbered from 1 to n, each with their own yearbook. They would like to pass their yearbooks around and get them signed by other students.

You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it includes the integers from 1 to n exactly once each, in some order). The meaning of this list is described below.

Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute: Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), and then they'll pass it to student arr[i-1]. It's possible that arr[i-1] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.

It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook back and will never end up holding more than one yearbook at a time.

You must compute a list of n integers output, whose element at i-1 is equal to the number of signatures that will be present in student i's yearbook once they receive it back.

III. Contiguous Subarrays

You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:

- The value at index i must be the maximum element in the contiguous subarrays, and

- These contiguous subarrays must either start from or end on index i.

HEAPS

I. Largest Triple Products

You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the product of the three largest elements out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).

Note that the three largest elements used to form any product may have the same values as one another, but they must be at different indices in arr.

II. Magical Candy Bags

You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish, the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that floor(x/2) pieces are now inside.

You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?

III. Median Stream

You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the median of the elements arr[0..i] (rounded down to the nearest integer).

The median of a list of integers is defined as follows. If the integers were to be sorted, then:

- If there are an odd number of integers, then the median is equal to the middle integer in the sorted order.

- Otherwise, if there are an even number of integers, then the median is equal to the average of the two middle-most integers in the sorted order.

GREEDY ALGORITHMS

I. Slow Sums

Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number: Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal to the value of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.

For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. The goal in this problem is to find the highest possible penalty for a given input.

II. Element Swapping

Given a sequence of n integers arr, determine the lexicographically smallest sequence which may be obtained from it after performing at most k element swaps, each involving a pair of consecutive elements in the sequence.

Note: A list x is lexicographically smaller than a different equal-length list y if and only if, for the earliest index at which the two lists differ, x's element at that index is smaller than y's element at that index.

III. Seating Arrangements

There are n guests attending a dinner party, numbered from 1 to n. The ith guest has a height of arr[i-1] inches.
The guests will sit down at a circular table which has n seats, numbered from 1 to n in clockwise order around the table. As the host, you will choose how to arrange the guests, one per seat. Note that there are n! possible permutations of seat assignments.

Once the guests have sat down, the awkwardness between a pair of guests sitting in adjacent seats is defined as the absolute difference between their two heights. Note that, because the table is circular, seats 1 and n are considered to be adjacent to one another, and that there are therefore n pairs of adjacent guests.

The overall awkwardness of the seating arrangement is then defined as the maximum awkwardness of any pair of adjacent guests. Determine the minimum possible overall awkwardness of any seating arrangement.

TREES

I. Number of Visible Nodes

There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes at each level. Return the number of visible nodes.

Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.

II. Nodes in a Subtree

You are given a tree that contains N nodes, each containing an integer u which corresponds to a lowercase character c in the string s using 1-based indexing.

You are required to answer Q queries of type [u, c], where u is an integer and c is a lowercase letter. The query result is the number of nodes in the subtree of node u containing c.

SEARCH

I. Revenue Milestones

We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones. Given an array of the revenue on each day, and an array of milestones Facebook wants to reach, return an array containing the days on which Facebook reached every milestone.

II. 1 Billion Users

We have N different apps with different user growth rates. At a given time t, measured in days, the number of users using an app is g^t (for simplicity we'll allow fractional users), where g is the growth rate for that app. These apps will all be launched at the same time and no user ever uses more than one of the apps. We want to know how many total users there are when you add together the number of users from each app.

After how many full days will we have 1 billion total users across the N apps?

RECURSION

I. Encrypted Words

You've devised a simple encryption method for alphabetic strings that shuffles the characters in such a way that the resulting string is hard to quickly read, but is easy to convert back into the original string.
When you encrypt a string S, you start with an initially-empty resulting string R and append characters to it as follows:

- Append the middle character of S (if S has even length, then we define the middle character as the left-most of the two central characters)

- Append the encrypted version of the substring of S that's to the left of the middle character (if non-empty)

- Append the encrypted version of the substring of S that's to the right of the middle character (if non-empty)

For example, to encrypt the string "abc", we first take "b", and then append the encrypted version of "a" (which is just "a") and the encrypted version of "c" (which is just "c") to get "bac".

If we encrypt "abcxcba" we'll get "xbacbca". That is, we take "x" and then append the encrypted version "abc" and then append the encrypted version of "cba".

II. Change in a Foreign Currency

You likely know that different currencies have coins and bills of different denominations. In some currencies, it's actually impossible to receive change for a given amount of money. For example, Canada has given up the 1-cent penny. If you're owed 94 cents in Canada, a shopkeeper will graciously supply you with 95 cents instead since there exists a 5-cent coin.

Given a list of the available denominations, determine if it's possible to receive exact change for an amount of money targetMoney. Both the denominations and target amount will be given in generic units of that currency.

SORTING

I. Balanced Split

Given an array of integers (which may include repeated integers), determine if there's a way to split the array into two subsequences A and B such that the sum of the integers in both arrays is the same, and all of the integers in A are strictly smaller than all of the integers in B.

Note: Strictly smaller denotes that every integer in A must be less than, and not equal to, every integer in B.

II. Counting Triangles

Given a list of N triangles with integer side lengths, determine how many different triangles there are. Two triangles are considered to be the same if they can both be placed on the plane such that their vertices occupy exactly the same three points.

STACKS

I. Balance Brackets

A bracket is any of the following characters: (, ), {, }, [, or ].

We consider two brackets to be matching if the first bracket is an open-bracket, e.g., (, {, or [, and the second bracket is a close-bracket of the same type. That means ( and ), [ and ], and { and } are the only pairs of matching brackets.

Furthermore, a sequence of brackets is said to be balanced if the following conditions are met:

1) The sequence is empty, or

2) The sequence is composed of two or more non-empty sequences, all of which are balanced, or

3) The first and last brackets of the sequence are matching, and the portion of the sequence without the first and last elements is balanced.

You are given a string of brackets. Your task is to determine whether each sequence of brackets is balanced. If a string is balanced, return true, otherwise, return false

HASH TABLE

I. Pair Sums

Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.

If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.

QUEUES

I. Queue Removals

You're given a list of n integers arr, which represent elements in a queue (in order from front to back). You're also given an integer x, and must perform x iterations of the following 3-step process:

1) Pop x elements from the front of queue (or, if it contains fewer than x elements, pop all of them)

2) Of the elements that were popped, find the one with the largest value (if there are multiple such elements, take the one which had been popped the earliest), and remove it

3) For each one of the remaining elements that were popped (in the order they had been popped), decrement its value by 1 if it's positive (otherwise, if its value is 0, then it's left unchanged), and then add it back to the queue

Compute a list of x integers output, the ith of which is the 1-based index in the original array of the element which had been removed in step 2 during the ith iteration.

GRAPHS

I. Minimizing Permutations

In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:

Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.

Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.

LINKED LIST

I. Reverse Operations

You are given a singly-linked list that contains N integers. A subpart of the list is a contiguous set of even elements, bordered either by either end of the list or an odd element. For example, if the list is [1, 2, 8, 9, 12, 16], the subparts of the list are [2, 8] and [12, 16].

Then, for each subpart, the order of the elements is reversed. In the example, this would result in the new list, [1, 8, 2, 9, 16, 12].

The goal of this question is: given a resulting list, determine the original order of the elements.

