from gensim.models import Word2Vec
topics = [
    ["cricket", "bat", "ball", "wicket", "stump", "umpire", "run", "boundary", "six", "over"],
    ["football", "goal", "pitch", "referee", "kick", "pass", "card", "penalty", "offside", "foul"],
    ["hockey", "ice", "puck", "stick", "skate", "rink", "goalie", "net", "period", "penalty"],
    ["chess", "board", "king", "queen", "rook", "bishop", "knight", "pawn", "checkmate", "move"],
]
model = Word2Vec(sentences=topics,
                epochs = 10000,
                vector_size = 100,
                window = 3,
                min_count = 1,
                sg = 1)

print(model.wv.most_similar("chess",topn=1))
print(model.wv.most_similar("hockey",topn=4))
print(model.wv.most_similar("kick",topn=2))
print(model.wv.most_similar("run",topn=3))

