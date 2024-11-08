#include <iomanip>
#include <iostream>
#include <thread>
#include <vector>
#pragma GCC target("popcnt")
using namespace std;

#define RESULT_MOD 1000

int THREAD_COUNT = 16;

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

void calc(int start, int end, int n, int t, int bit_itr, vector<int> &count,
          vector<vector<unsigned long long>> &bit) {
    int i = start, j, l, both;
    for (; i < end; i++) {
        for (j = i + 1; j < n; j++) {
            both = 0;
            for (l = 0; l < bit_itr; l++) {
                both += __builtin_popcountll(bit[i][l] & bit[j][l]);
            }
            if (both >= t) {
                count[i]++;
                count[j]++;
            }
        }
    }
}

void calc2(int i, int start, int end, int n, int t, int bit_itr,
           vector<int> &count, vector<vector<unsigned long long>> &bit) {
    int j = start, l, both;
    for (; j < end; j++) {
        both = 0;
        for (l = 0; l < bit_itr; l++) {
            both += __builtin_popcountll(bit[i][l] & bit[j][l]);
        }
        if (both >= t) {
            count[i]++;
            count[j]++;
        }
    }
}

int main(int argc, char **argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    if (argc > 1)
        THREAD_COUNT = stoi(argv[1]);

    int MAX_N, MAX_M;
    cin >> MAX_N >> MAX_M;
    MAX_M += 63;

    int z, n, m, t, u, k, both, special, a, i, j, l, bit_itr, t_itr, avg, r,
        offset, MAX_BITS_SIZE = MAX_M >> 6;

    vector<int> count(MAX_N, 0);

    vector<vector<unsigned long long>> bit(
        MAX_N, vector<unsigned long long>(MAX_BITS_SIZE, 0));

    cin >> z;
    string s;
    vector<thread> threads(THREAD_COUNT);
    while (z--) {

        cin >> n >> m >> t >> u >> k;

        for (i = 0; i < n; i++) {
            cin >> s;
            for (j = 0; j < m; j++) {
                bit[i][j >> 6] = bit[i][j >> 6] | ((s[j] - '0') << (j & 0x3F));
            }
        }

        bit_itr = (m + 63) >> 6;

        avg = n / THREAD_COUNT;
        r = n % THREAD_COUNT;
        offset = 0;
        for (i = 0; i < THREAD_COUNT; i++) {
            if (r > 0) {
                threads[i] =
                    thread(calc, avg * i + offset, avg * (i + 1) + 1 + offset,
                           n, t, bit_itr, ref(count), ref(bit));
                r--;
                offset++;
            } else {
                threads[i] =
                    thread(calc, avg * i + offset, avg * (i + 1) + offset, n, t,
                           bit_itr, ref(count), ref(bit));
            }
        }
        for (auto &th : threads)
            th.join();

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