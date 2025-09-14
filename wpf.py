import subprocess
import json

data = subprocess.check_output(["curl", "-X", "GET", "\\", "https://datasets-server.huggingface.co/rows?dataset=roneneldan%2FTinyStories&config=default&split=train&offset=0&length=100"])

def parse_data(data):
    rows = json.loads(data)["rows"]
    texts = [row["row"]["text"] for row in rows]
    res = ""

    for text in texts:
        res += text + "\n"

    return res.encode("utf-8")

open("e.txt", "wb").write(parse_data(data))

def create_wpf(filepath):
    contents = open(filepath, "r").read()
    words = contents.split(" ")

    first = words[0].split('\n')[0].replace("\t", "")

    # for sentence in contents.split("\n"):
    #     word = sentence.split(" ")[0]
    #     res += f"{word}\n{words.count(word)}\n"
    res = f"{first}\n{words.count(words[0])}\n"

    for i, word in enumerate(words):
        if i < len(words) - 2:
            w = [words[i+x].split('\n')[0].replace("\t", "") for x in range(3)]
            res += f"{w[0]} {w[1]} {w[2]}\n{words.count(word)} {words.count(words[i+1])} {words.count(words[i+2])}\n"
    
    return res[:-1]

open("wpf.dat", "w").write(create_wpf("e.txt"))