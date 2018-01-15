def check(self):

  for i in range(0,4):

    for j in range(0,4):

      if self.plateau[i,j] == 2048:

        print("Vous avez gagné!")

      elif self.plateau