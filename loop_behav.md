```python
x = 10

for x in range(5):
    pass

print(x) # 4 not 10 
```



### Never reuse important variable names as loop variables

```python
x = 10

for i in range(5):
    print(i)

print(x)  # 10

```

