from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ["running", "runs", "runner", "runners", "walked", "walking", "walks", "walker", "playing", "played", "plays", "player", "studying", "studied", "studies", "studying", "writing", "written", "writes", "writer", "reading", "reads", "reader", "readable", "jumping", "jumped", "jumps", "jumper", "singing", "sang", "sings", "singer", "driving", "driven", "drives", "driver", "talking", "talked", "talks", "talkative", "computing", "computed", "computer", "computation", "connecting", "connected", "connection", "connections", "organizing", "organization"]
list = [] #empty list
for item in words:
    list.append(ps.stem(item))
print(list)

