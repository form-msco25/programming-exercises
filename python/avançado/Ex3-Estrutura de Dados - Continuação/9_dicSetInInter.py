"""Use um dicionário onde valores são sets (ex.: tags: set de palavras-chave);
adicione tags a um post e verifique overlaps com in e interseção."""
posts = {"post1": {"python", "programação", "tutorial"},"post2": {"receita", "culinária", "dicas"}}
post_alvo = "post1"
novas_tags = {"iniciantes", "exemplos"}
if post_alvo in posts:
    posts[post_alvo].update(novas_tags)
else:
    posts[post_alvo] = novas_tags
print(f"Tags atualizadas:\n{post_alvo}: {posts[post_alvo]}")
tags_comparacao = {"tutorial", "dicas", "exemplos"}
overlap = posts[post_alvo] & tags_comparacao
if overlap:
    print(f"As tags {overlap} aparecem tanto no post quanto no conjunto de comparação.")
else:
    print("Não há tags em comum.")
tag_especifica = "python"
if tag_especifica in posts[post_alvo]:
    print(f"A tag '{tag_especifica}' existe no post.")
else:
    print(f"A tag '{tag_especifica}' não existe no post.")