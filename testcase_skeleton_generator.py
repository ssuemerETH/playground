def main():
    # both bounds inclusive
    min = 35
    max = 50

    lines = []

    with open("sample_template.txt", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
    
    for i in range(min, max + 1):
        with open(f"rest/T{i}.java", "w") as f:
            for line in lines:
                f.write(line.replace("$num$", str(i)))
    

if __name__ == "__main__":
    main()

