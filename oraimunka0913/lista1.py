#!/usr/bin/env python3
a = [1, None, ["a", "b"], "szoveg", 256, 0]
b = a
a[0] = 12
print(b)
print(b[:])
