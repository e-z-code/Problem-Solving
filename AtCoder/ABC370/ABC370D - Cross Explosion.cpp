/*
ABC370D - Cross Explosion (https://atcoder.jp/contests/abc370/tasks/abc370_d)

There is an R X C grid A. Initially, there is one wall in each cell.
You are given Q queries with the format of (i, j).
If there is a wall at A[i][j], the query will destroy the wall.
If there is no wall at A[i][j], the query will destroy the first walls that appear when looking up, down, left, and right.
Calculate the number of remaining walls after all queries.
*/

#include <iostream>
#include <set>
#include <vector>

using namespace std;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    // 1. TO GET THE INPUT
    
    int row_count, col_count, query_count;
    cin >> row_count >> col_count >> query_count;

    vector<set<int>> row(row_count), col(col_count);
    for (int row_num = 0; row_num < row_count; row_num++) {
        for (int col_num = 0; col_num < col_count; col_num++) {
            row[row_num].insert(col_num);
            col[col_num].insert(row_num);
        }
    }

    
    // 2. TO PROCESS QUERIES

    for (int query_num = 0; query_num < query_count; query_num++) {

        int row_num, col_num;
        cin >> row_num >> col_num;
        row_num--;
        col_num--;

        if (row[row_num].count(col_num)) {
            row[row_num].erase(col_num);
            col[col_num].erase(row_num);
            continue;
        }

        auto addr = col[col_num].lower_bound(row_num);
        if (addr != begin(col[col_num])) {
            int row_val = *prev(addr);
            row[row_val].erase(col_num);
            col[col_num].erase(row_val);
        }

        addr = col[col_num].lower_bound(row_num);
        if (addr != end(col[col_num])) {
            int row_val = *addr;
            row[row_val].erase(col_num);
            col[col_num].erase(row_val);
        }

        addr = row[row_num].lower_bound(col_num);
        if (addr != begin(row[row_num])) {
            int col_val = *prev(addr);
            row[row_num].erase(col_val);
            col[col_val].erase(row_num);
        }

        addr = row[row_num].lower_bound(col_num);
        if (addr != end(row[row_num])) {
            int col_val = *addr;
            row[row_num].erase(col_val);
            col[col_val].erase(row_num);
        }

    }

    
    // 3. TO SOLVE THE PROBLEM

    int ans = 0;
    for (int row_num = 0; row_num < row_count; row_num++) {
        ans += row[row_num].size();
    }
    cout << ans << "\n";
    return 0;
}