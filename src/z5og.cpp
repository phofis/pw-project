#include <bits/stdc++.h>
#pragma GCC optimize("03")
#pragma GCC target("popcnt")
using namespace std;

int pot(int a, int b) {
    if (b == 1)
        return a % 1000;
    if (b & 1)
        return (pot((a * a) % 1000, b >> 1) * a) % 1000;
    return pot((a * a) % 1000, b >> 1) % 1000;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int z, n, m, t, u, k, both, special, a, MAX_N, MAX_M;

    cin >> MAX_N >> MAX_M;

    MAX_M += 15;

    int pre[0xFFFF + 7];
    for (int i = 0; i <= 0xFFFF; i++) {
        pre[i] = __builtin_popcount(i);
    }

    int count[MAX_N];

    int **bit = new int *[MAX_N];
    for (int i = 0; i < MAX_N; i++) {
        bit[i] = new int[MAX_M >> 4];
    }

    cin >> z;
    string s;
    while (z--) {

        cin >> n >> m >> t >> u >> k;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < (m + 15) >> 4; j++) {
                bit[i][j] = 0;
            }
        }

        for (int i = 0; i < n; i++) {
            cin >> s;
            for (int j = 0; j < m; j++) {
                bit[i][j >> 4] =
                    bit[i][j >> 4] | ((int)(s[j] - '0') << (j & 0xF));
            }
        }

        special = 0;
        memset(count, 0, sizeof(count));
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                both = 0;
                for (int l = 0; l < (m + 15) >> 4; l++) {
                    both += pre[bit[i][l] & bit[j][l]];
                }
                if (both >= t) {
                    count[i]++;
                    count[j]++;
                }
            }
        }
        for (int i = 0; i < n; i++)
            if (count[i] >= u)
                special++;
        cout << special << " " << setfill('0') << setw(3) << pot(special, k)
             << endl;
    }
    for (int i = 0; i < MAX_N; i++) {
        delete[] bit[i];
    }
    delete[] bit;
}