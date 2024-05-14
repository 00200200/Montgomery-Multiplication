#include <iostream>
#include <chrono>

using ll = long long;


class MontgomeryReducer {
private:
    ll mod;
    ll reducerbits;
    ll reducer;
    ll mask;
    ll r_inv;
    ll k;

    ll gcdExtended(ll a, ll b, ll* x, ll* y) {
        if (a == 0)
        {
            *x = 0;
            *y = 1;
            return b;
        }

        ll x1, y1;
        ll gcd = gcdExtended(b % a, a, &x1, &y1);

        *x = y1 - (b / a) * x1;
        *y = x1;

        return gcd;
    }

public:
    MontgomeryReducer(ll mod);
    ll convert_in(ll value);
    ll convert_out(ll value);
    ll multiply(ll value1, ll value2);
};

MontgomeryReducer::MontgomeryReducer(ll mod) {
    this->mod = mod;
    reducer = 2;
    reducerbits = 1;
    while (reducer < mod) {
        reducer *= 2;
        reducerbits++;
    }
    mask = reducer - 1;

    ll x, y;
    ll temp = gcdExtended(reducer, mod, &x, &y);
    this->r_inv = (x + mod) % mod;
    this->k = (reducer * r_inv - 1) / mod;
}

ll MontgomeryReducer::convert_in(ll value) {
    return (value << reducerbits) % mod;
}

ll MontgomeryReducer::convert_out(ll value) {
    return (value * r_inv) % mod;
}

ll MontgomeryReducer::multiply(ll value1, ll value2) {
    ll x = value1 * value2;
    ll s = (x * k) & mask; // zamiat % reducer uzywamy & mask
    ll t = x + s * mod;
    ll u = t >> reducerbits; // dzielenie przez reducer
    if (u < mod)
        return u;
    return u - mod;
}

double montgomery_multipliaction_benchmark(ll n, ll a, ll b) {
    MontgomeryReducer mr = MontgomeryReducer(n);
    ll a_m = mr.convert_in(a);
    ll b_m = mr.convert_in(b);
    ll product;
    auto start = std::chrono::steady_clock::now();
    for (ll i = 0; i < 2000000; i++)
        product = mr.multiply(a_m, b_m);
   
    auto end = std::chrono::steady_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    ll ans = mr.convert_out(product);
    return (double)duration.count();
}

double naive_solution_benchmark(ll n, ll a, ll b) {
    ll product;
    auto start = std::chrono::steady_clock::now();
    for (ll i = 0; i < 2000000; i++)
        product = (a * b) % n;
    
    auto end = std::chrono::steady_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    return (double)duration.count();
}

int main() {
    ll n = 1e9 + 7;
    ll a = 12345678901234567;
    ll b = 67234888823623901;

    double num_of_benchmarks = 100, m_sum = 0, n_sum = 0;
    for (int i = 0; i < num_of_benchmarks; i++) {
        m_sum = montgomery_multipliaction_benchmark(n, a, b);
        n_sum = naive_solution_benchmark(n, a, b);
    }

    std::cout << m_sum / num_of_benchmarks << "\n";
    std::cout << n_sum / num_of_benchmarks << "\n";


    return 0;
}
