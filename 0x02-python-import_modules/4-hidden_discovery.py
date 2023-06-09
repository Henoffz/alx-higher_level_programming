#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    for i in range(len(name)):
        if name[i][:2] != "__":
            print(name[i])
