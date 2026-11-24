#include <iostream>
#include <vector>

constexpr long long modulus = 1'000'000'007;

long long count_paths(int target, int largest_weight) {
    std::vector<long long> ways(target + 1, 0);
    ways[0] = 1;

    for (int total = 1; total <= target; ++total) {
        for (int weight = 1; weight <= largest_weight && weight <= total; ++weight) {
            ways[total] = (ways[total] + ways[total - weight]) % modulus;
        }
    }
    return ways[target];
}

int main() {
    int n, k, d;
    if (!(std::cin >> n >> k >> d)) return 1;

    const long long all = count_paths(n, k);
    const long long small = count_paths(n, d - 1);
    std::cout << (all - small + modulus) % modulus << '\n';
}
