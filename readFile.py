# .game file structure

# gamename
# list of icon file adresses, seperated by comma
# executable path
# Auther [NAME - DATE]
# Description for all remaining lines...
# ...


import os

class Game:
  name = ""
  images = ""
  executable = ""
  auther = ""
  description = ""

  def __init__(self, name, images, executable, auther, description):
    self.name = name
    self.images = images
    self.executable = executable
    self.auther = auther
    self.description = description

  def launch(self):
    os.system("./", self.executable)


def getGames():
  list = os.listdir("./gameslist/")
  games = []
  for file in list:
    with open("./gameslist/" + file, "r") as f:
      raw = f.read()
      f.close()

    lines = raw.split("\n")
    description = ""
    for x in range(4, len(lines)):
      description += "\n" + lines[x]
    games.append(Game(lines[0], lines[1].split(","), lines[2], lines[4], description))

  return games

