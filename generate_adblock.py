import datetime

INPUT_FILE = "filters.txt"
OUTPUT_FILE = "adblock_list.txt"

def main():
    # lê linhas do arquivo, preserva comentários e ignora vazias
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw = [line.rstrip() for line in f if line.strip()]

    seen = set()
    filters = []
    for line in raw:
        if line.startswith("!") or line.startswith("#"):
            filters.append(line)
            continue
        if line not in seen:
            seen.add(line)
            filters.append(line)

    # pega data atual UTC
    now = datetime.datetime.utcnow()
    version = now.strftime("%Y%m%d%H%M")  # timestamp YYYYMMDDHHMM
    last_modified = now.strftime("%d %b %Y %H:%M UTC")  # ex: 20 Sep 2025 21:30 UTC

    # cabeçalho no padrão Adblock Plus 2.0
    header = [
        "[Adblock Plus 2.0]",
        f"! Version: {version}",
        "! Title: PT-BR FILTER",  # você pode trocar o título aqui
        f"! Last modified: {last_modified}",
        "! Expires: 1 days (update frequency)",
        "!",
    ]

    # escreve arquivo final
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(header + filters) + "\n")

if __name__ == "__main__":
    main()
