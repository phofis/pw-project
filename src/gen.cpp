#include <chrono>
#include <iostream>
#include <random>
using namespace std;

int rand(int a, int b) { return a + (lrand48() % (b - a + 1)); }

int main() {
    auto now = chrono::high_resolution_clock::now();
    auto duration =
        chrono::duration_cast<chrono::nanoseconds>(now.time_since_epoch());
    srand48(duration.count() ^ 0xabcdef);
    int z;
    cin >> z;
    int MAX_N;
    cin >> MAX_N;
    int MIN_N = MAX_N / 10;
    int MAX_M;
    cin >> MAX_M;
    int MIN_M = MAX_M / 10;

    int n, m, t, u, k, i;
    string s;
    cout << MAX_N << ' ' << MAX_M << '\n';
    cout << z << '\n';
    while (z--) {
        n = rand(MIN_N, MAX_N);
        m = rand(MIN_M, MAX_M);
        t = rand(1, m);
        u = rand(1, n - 1);
        k = rand(1, 1e9);
        cout << n << ' ' << m << ' ' << t << ' ' << u << ' ' << k << '\n';
        s.resize(m, 0);
        for (i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                s[j] = (lrand48() & 1) + '0';
            }
            cout << s << '\n';
        }
    }
}