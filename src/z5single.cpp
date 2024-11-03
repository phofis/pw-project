#include <iomanip>
#include <iostream>
#include <vector>
#pragma GCC target("popcnt")
using namespace std;

#define RESULT_MOD 1000

int pot(int base, int exp) {
    if (base == 0)
        return 0;
    int result = 1;
    base = base % RESULT_MOD;
    while (exp > 0) {
        if (exp & 1)
            result = (result * base) % RESULT_MOD;
        exp = exp >> 1;
        base = (base * base) % RESULT_MOD;
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int MAX_N, MAX_M;
    cin >> MAX_N >> MAX_M;
    MAX_M += 63;

    int z, n, m, t, u, k, both, special, a, i, j, l, bit_itr,
        MAX_BITS_SIZE = MAX_M >> 6;

    vector<int> count(MAX_N, 0);

    vector<vector<unsigned long long>> bit(
        MAX_N, vector<unsigned long long>(MAX_BITS_SIZE, 0));

    cin >> z;
    string s;
    while (z--) {
        cin >> n >> m >> t >> u >> k;

        for (i = 0; i < n; i++) {
            cin >> s;
            for (j = 0; j < m; j++) {
                bit[i][j >> 6] |=
                    (((unsigned long long)s[j] - '0') << (j & 0x3F));
            }
        }

        bit_itr = (m + 63) >> 6;

        for (i = 0; i < n; i++) {
            for (j = i + 1; j < n; j++) {
                both = 0;
                for (l = 0; l < bit_itr; l++) {
                    both += __builtin_popcountll((bit[i][l]) & (bit[j][l]));
                }
                if (both >= t) {
                    count[i]++;
                    count[j]++;
                }
            }
        }
        for (i = 0; i < n; i++)
            if (count[i] >= u)
                special++;
        cout << special << ' ' << setfill('0') << setw(3) << pot(special, k)
             << '\n';

        for (i = 0; i < n; i++) {
            bit[i].assign(MAX_BITS_SIZE, 0);
        }
        special = 0;
        count.assign(MAX_N, 0);
    }
}