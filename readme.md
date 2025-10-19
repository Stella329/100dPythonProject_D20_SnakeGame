KNOWLEDGE_snake:
- Note: here it doesn't use class inheritance to create the class
- python Constants: don't like the hard-coded piece of text inside the body of a program
- create snake class: call the method in __init__
slice

KNOW_food
- AIM: create food body; make it move; define the collision
- inherit Turtle() into Food: food is a turtle object
- turtle.distance(): use it to detect the collision of snake.head with food
  - define in main game control: in main.py
  food position: random coor and refresh 
  - posistion: 不能在screen边缘

KNOW_scoreboard
- AIM: mainly do the writings on Screen
- fun: turtle.write() + turtle.clear()