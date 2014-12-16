def comprehension(n):
  squares = [k*k for k in range(1, n+1)]

  factors = [k for k in range(1, n+1) if n % k == 0]

  return squares, factors

print(comprehension(100))
