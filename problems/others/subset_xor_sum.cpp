// Link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/

// Topics: Backtracking, Bit Manipulation, Combinatorics, Enumeration

// Using mask
#include <iostream>
#include <vector>
#include <numeric>
#include <execution>

class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int total_xors = 0;
        int size_nums = nums.size();
        int nb_subsets = 1 << size_nums;

        for (int subset_index = 1; subset_index <= nb_subsets; subset_index++) {
            int subset_xor = 0;
            for (int i = 0; i < size_nums; i++) {
                if ((1 << i) & subset_index) {
                    subset_xor ^= nums[i];
                }
            }
            total_xors += subset_xor;
        }
        return total_xors;
    }
};

// Recursion

