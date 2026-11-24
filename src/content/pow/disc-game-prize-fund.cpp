#include <array>
#include <iostream>

int main() {
  constexpr unsigned turns = 15;
  std::array<std::array<unsigned long long, turns + 1>, turns + 1> weights{};
  weights[0][0] = 1;
  unsigned long long denominator = 1;

  for (unsigned turn = 1; turn <= turns; ++turn) {
    denominator *= turn + 1;
    for (unsigned blues = 0; blues <= turn; ++blues) {
      weights[turn][blues] = turn * weights[turn - 1][blues];
      if (blues > 0) {
        weights[turn][blues] += weights[turn - 1][blues - 1];
      }
    }
  }

  unsigned long long winning_weight = 0;
  for (unsigned blues = turns / 2 + 1; blues <= turns; ++blues) {
    winning_weight += weights[turns][blues];
  }
  std::cout << denominator / winning_weight << '\n';
}
