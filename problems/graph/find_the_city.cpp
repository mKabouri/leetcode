// Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        // Floyd-Warshall algorithm
        // Initialization step
        vector<vector<int>> dist_matrix(n, vector<int>(n, INT_MAX));
        for (int i = 0; i < n; i++) {
            dist_matrix[i][i] = 0;
        }
        for (vector<int>& edge : edges) {
            dist_matrix[edge[0]][edge[1]] = edge[2];
            dist_matrix[edge[1]][edge[0]] = edge[2];
        }
        // Distance computation
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist_matrix[i][k] != INT_MAX && dist_matrix[k][j] != INT_MAX) {
                        dist_matrix[i][j] = min(
                            dist_matrix[i][j],
                            dist_matrix[i][k] + dist_matrix[k][j]
                        );
                    }
                }
            }
        }
        // Find the city!
        int city = -1;
        int best_num_neighbors = n;
        for (int i = 0; i < n; i++) {
            int num_reachable_cities = 0;
            for (int j = 0; j < n; j++) {
                if (j != i && dist_matrix[i][j] <= distanceThreshold) {
                    num_reachable_cities += 1;
                }
            }
            if (num_reachable_cities <= best_num_neighbors) {
                best_num_neighbors = num_reachable_cities;
                city = i;
            }
        }
        return city;
    }
};
