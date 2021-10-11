import random

#equazione generale della retta y = mx + q
def f(x):
  return 1 * x + 0.2

def sign(guess):
  if guess >= 0:
    return 1
  else:
    return -1

class perceptron():
  def __init__(self, input0, input1, answer):
    self.input0 = input0
    self.input1 = input1
    self.bias1 = 1
    self.answer1 = answer
    self.somma1 = 0
    self.LR1 = 0.1
    self.error1 = 0

  def W(self):
    self.w0 = random.randint(-1, 1)
    self.w1 = random.randint(-1, 1)
    self.w3 = random.randint(-1, 1)

  def somma(self):
    self.somma1 = self.input0 * self.w0 + self.input1 * self.w1 + self.bias1 * self.w3
    self.somma1 = sign(self.somma1)
    return self.somma1

  def training(self):
    self.error1 = self.answer1 - self.somma1
    self.w0 += self.error1 * self.input0 * self.LR1
    self.w1 += self.error1 * self.input1 * self.LR1
    self.w3 += self.error1 * self.bias1 * self.LR1

class point():
  def __init__(self):
    self.x = random.randint(0, 400)
    self.y = random.randint(0, 400)
    #confronta la y del punto con l'altezza della retta e la y del punto
    lineY = f(self.x)
    #dati di training
    if self.y < lineY:
      self.guess = 1
    else:
      self.guess = -1

points = []
for i in range(100):
  points.append(point())

p = perceptron(0, 0, 0)
p.W()
index = 0
for x in points:
  p.__init__(points[index].x, points[index].y, points[index].guess)
  p.somma()
  p.training()
  index += 1

#prova del neurone allenato
p.__init__(100, 50, 1)
print(p.error1)
print(p.somma())
