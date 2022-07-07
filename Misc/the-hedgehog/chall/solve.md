In this challenge we are requested to input a simple json array. Each element is matched against the reges `^[a-z]+$`. If not, then the program exits. If it does, then the strings get executed using os.system using the md5sum command. We can calculate the md5sum of `flag` but not actually read the file. 

It just so happens to be the case that most regex implementations are made to match against a single line. Meaning if a string ends on a new line character it will still match almost any pattern, giving us a possible solution:

```python
['a\n', 'cat', 'flag']
```