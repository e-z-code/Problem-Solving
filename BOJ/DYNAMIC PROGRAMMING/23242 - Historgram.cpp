/*
23242 - Histogram (https://www.acmicpc.net/problem/23242)

There is a histogram of length N.
If you choose a bucket [L, R], the average value of the bucket becomes the representative value for the range.
Given a histogram and the number of buckets, find a minimum error histogram.
*/

#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    // 1. TO GET THE INPUT

    int bucket_count, num_count;
    cin >> bucket_count;
    cin >> num_count;

    int histogram[num_count+1];
    for (int num = 1; num <= num_count; num++) {
        int frequency;
        cin >> frequency;
        histogram[num] = frequency;
    }


    // 2. PREFIX SUM

    vector<int> prefix_sum(1);
    vector<int> prefix_sum_squared(1);
    for (int num = 1; num <= num_count; num++) {
        prefix_sum.push_back(prefix_sum.back() + histogram[num]);
        prefix_sum_squared.push_back(prefix_sum_squared.back() + pow(histogram[num], 2));
    }


    // 3. DYNAMIC PROGRAMMING
    // dp[i][j] = Minimum sum of variances when you divided 1 ~ j into i buckets

    double dp[bucket_count+1][num_count+1];
    for (int bucket = 1; bucket <= bucket_count; bucket++) {
        for (int num = 1; num <= num_count; num++) {

            if (bucket > num) {
                continue;
            } else if (bucket == num) {
                dp[bucket][num] = 0;
            } else {
                // V(X) = E(pow(X, 2)) - pow(E(X), 2)
                double mean_squared, squared_mean, variance;
                if (bucket == 1) {
                    mean_squared = (double) (prefix_sum_squared.at(num) - prefix_sum_squared.at(0)) / num;
                    squared_mean = pow((double) (prefix_sum.at(num) - prefix_sum.at(0)) / num, 2);
                    variance = mean_squared - squared_mean;
                    dp[bucket][num] = variance * num;
                } else {
                    double min_val = 2147483647;
                    for (int last_bucket_num = 1; last_bucket_num < num; last_bucket_num++) {
                        mean_squared = (double) (prefix_sum_squared.at(num) - prefix_sum_squared.at(last_bucket_num)) / (num - last_bucket_num);
                        squared_mean = pow((double) (prefix_sum.at(num) - prefix_sum.at(last_bucket_num)) / (num - last_bucket_num), 2);
                        variance = mean_squared - squared_mean;
                        min_val = min(min_val, dp[bucket-1][last_bucket_num] + variance * (num - last_bucket_num));
                    }
                    dp[bucket][num] = min_val;
                }
            }

        }
    }

    cout.precision(20);
    cout << dp[bucket_count][num_count];

}