import datetime

INPUT_FILE = "filters.txt"
OUTPUT_FILE = "adblock_list.txt"

def main():
    # lê filtros
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw = [line.strip() for line in f if line.strip()]

    # remove duplicados preservando ordem
    seen = set()
    filters = []
    for line in raw:
        if line.startswith("!") or line.startswith("#"):
            continue
        if line not in seen:
            seen.add(line)
            filters.append(line)

    # gera cabeçalho
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    header = [
        "! Title: Minha Lista Adblock",
        "! Author: GitHub Actions",
        f"! Updated: {now}",
        "!",
    ]

    # escreve arquivo final
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(header + filters) + "\n")

if __name__ == "__main__":
    main()
