"""Crie dois sets com linguagens de programação (por exemplo, {'Python', 'Java'} e
{'C', 'Python'}). Mostre apenas as linguagens comuns."""

set_A = {"c", "c++", "c#", "cobol", "java", "java script", "python"}
set_B = {"c++", "c#", "java script", "python"}
set_C = set_A & set_B
print(f"Elementos em comum: {set_C}")