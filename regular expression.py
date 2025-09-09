import re

# re.search

text="Hello world"
print(re.search(r"world",text))

# re.match


text="Hello world"
print(re.match(r"Hello",text))

# re.findall

text1="i have 2 apples and 5 oranges."
print(re.findall(r"\d+",text1))

# re.finditer

text2="i have 2 apples and 5 oranges."
for match in re.finditer(r"\d+",text2):
    print(match.group(),"at",match.start())



# re.sub

text="Hello 123,welcome 456!"
print(re.sub(r"\d+","number",text))


# re.split

text="apple, orange; banana, grape"
print(re.split(r"[;,]",text))

# regex metacharacters

# .
# ^
# $
# []
# \
# `
# *
# +
# {n}
# {n,}
# {n,m}
# ()

# shorthand characters

# \d digit
# \D non digit
# \s whitespace
# \S non whitespace
# \w word char
# \W non word char

# grouping and capturing

text5="John:34,Alice:45,Bob:23"
print(re.findall(r"(\w+):(\d+)",text5))

# compiling regex

pattern=re.compile(r"\d+")
text="123 apples and 456 banana"
text6="123 apples and 456 banana"
print(pattern.findall(text))


# regex flags

# IGNORECASE OR I
text="HeLlo world"
print(re.search(r"hello",text,re.IGNORECASE))
# re.multiline or M
text="""first line
second line
third line
"""
print(re.findall(r""))




