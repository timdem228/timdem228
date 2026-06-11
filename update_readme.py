import random
import re
facts = [
    "no",
    "#1 femboy in world",
    "idi nahuy",
    "ilovesweatyfemboys123",
    "Firefox is your default browser. Good boy.",
    "bebebbebebebe",
    "lol",
    "nah",
    "bruh",
    "faaaaah",
    "ahhhh...",
    "my friend",
    "my husbend",
    "vtf",
    "lalalalalalala"
]
random_fact = random.choice(facts)
with open("README.md", "r", encoding="utf-8") as file:
    readme_content = file.read()
pattern = r'(⚡ \*\*Fun fact\*\*: \[).*?(\]\(https://nikwonder\.ru\)<br>)'
new_content = re.sub(pattern, rf'\g<1>{random_fact}\g<2>', readme_content)
with open("README.md", "w", encoding="utf-8") as file:
    file.write(new_content)
