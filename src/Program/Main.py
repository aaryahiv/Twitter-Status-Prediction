
def main():
    f = open('sample.txt')
    line_contents = f.read()
    print(line_contents)
    search_phrase = "eatshit"
    for line in f.readlines():
        line.split()
        if line.find(search_phrase) >= 0:
            print(line)
