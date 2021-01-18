Q1 = {
  "title" : "You are hiking in the woods when a storm hits...",
  "B1" : "Keep hiking",
  "B2" : "Find shelter",
  "num" : "Q1"
}
Q2 = {
  "title" : "The storm is getting worse...",
  "B1" : "Keep hiking",
  "B2" : "Find shelter",
  "num" : "Q2"
}
Q3 = {
  "title" : "A tree is struck by lightning and falls on you",
  "B1" : "Start Over",
  "B2" : "",
  "num" : "Q3"
}
Q4 = {
  "title" : "Looking for shelter do you...",
  "B1" : "Stand under a tree",
  "B2" : "Go into a nearby cave",
  "num" : "Q4"
}
Q5 = {
  "title" : "In the cave you stumble on a mother bear and her cubs. The bear kills you.",
  "B1" : "Start Over",
  "B2" : "",
  "num" : "Q5"
}
Q6 = {
  "title" : "The storm clears but you don't remember how to get out of the woods...",
  "B1" : "Try to call someone on your phone",
  "B2" : "Go back where you think you came from",
  "num" : "Q6"
}
Q7 = {
  "title" : "Your phone has no signal...",
  "B1" : "Try to call again",
  "B2" : "Go back where you think you came from",
  "num" : "Q7"
}
Q8 = {
  "title" : "You come across a fallen tree...",
  "B1" : "Climb over the tree",
  "B2" : "Go back in the other direction",
  "num" : "Q8"
}
Q9 = {
  "title" : "You come across a creek..",
  "B1" : "Try to swim across",
  "B2" : "Go back to the fallen tree",
  "num" : "Q9"
}
Q10 = {
  "title" : "You find a path...",
  "B1" : "Follow it",
  "B2" : "Don't Follow it",
  "num" : "Q10"
}
Q11 = {
  "title" : "You've made it back to civilization!",
  "B1" : "Start Over",
  "B2" : "",
  "num" : "Q11"
}
Q12 = {
  "title" : "You drown trying to swim across the creek.",
  "B1" : "Start Over",
  "B2" : "",
  "num" : "Q12"
}
Q13 = {
  "title" : "You now live as a hermit in the woods because you could never find your way out.",
  "B1" : "Start Over",
  "B2" : "",
  "num" : "Q13"
}

questions = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13]

def gen():
  # return make_page("Q2", "hi", "hi")
  # return "<a href "">hi</a>"
  for q in questions:
    make_page(q)
    
def nextQ1(pressed, qNum):
  if(qNum == "Q1"):
    return """<a href="Q2.html">%s</a>""" % pressed
  if(qNum == "Q2"):
    return """<a href="Q3.html">%s</a>""" % pressed
  if(qNum == "Q3"):
    return """<a href="Q1.html">%s</a>""" % pressed
  if(qNum == "Q4"):
    return """<a href="Q6.html">%s</a>""" % pressed
  if(qNum == "Q5"):
    return """<a href="Q1.html">%s</a>""" % pressed
  if(qNum == "Q6"):
    return """<a href="Q7.html">%s</a>""" % pressed
  if(qNum == "Q7"):
    return """<a href="Q7.html">%s</a>""" % pressed
  if(qNum == "Q8"):
    return """<a href="Q10.html">%s</a>""" % pressed
  if(qNum == "Q9"):
    return """<a href="Q12.html">%s</a>""" % pressed
  if(qNum == "Q10"):
    return """<a href="Q11.html">%s</a>""" % pressed
  if(qNum == "Q11"):
    return """<a href="Q1.html">%s</a>""" % pressed
  if(qNum == "Q12"):
    return """<a href="Q1.html">%s</a>""" % pressed
  if(qNum == "Q13"):
    return """<a href="Q1.html">%s</a>""" % pressed
 
   
def nextQ2(pressed, qNum):
  if(qNum == "Q1" or qNum == "Q2"):
    return """<a href="Q4.html">%s</a>""" % pressed
  if(qNum == "Q4"):
    return """<a href="Q5.html">%s</a>""" % pressed
  if(qNum == "Q6"):
    return """<a href="Q8.html">%s</a>""" % pressed
  if(qNum == "Q7"):
    return """<a href="Q8.html">%s</a>""" % pressed
  if(qNum == "Q8"):
    return """<a href="Q9.html">%s</a>""" % pressed
  if(qNum == "Q9"):
    return """<a href="Q8.html">%s</a>""" % pressed
  if(qNum == "Q10"):
    return """<a href="Q13.html">%s</a>""" % pressed
   
def make_page(q):
  html = """<!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
  </head>
  <body>
    <h1>%s</h1>
    <button type="button">%s</button>
    <button type="button">%s</button>
    
  </body>
  </html>""" %  (q["title"],nextQ1(q["B1"],q["num"]),nextQ2(q["B2"],q["num"]))
  f = open(q["num"] + ".html", "w")
  f.write(html)
  f.close()
  
gen()

