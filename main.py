from src.genderizerQc import GenderizerQc

if __name__ == "__main__":
    genderizer = GenderizerQc()
    print(genderizer.genderize(["maxime", "claude", "jeremie", "danielle", "vanessa"]))
