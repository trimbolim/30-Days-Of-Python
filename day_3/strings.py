print ("'python' is {0} chars long".format(len('python')))
print ("'dragon' is {0} chars long".format(len('dragon')))

print ("dragon and python are not the same length: ", len('dragon') is not len('python'))

print ("on is found in dragon and python", "on" in "dragon" and "on" in "python" )

sentence = "I hope this course is not full of jargon"

print ("jargon does not appear in ", sentence, "jargon" not in sentence)

lp = len("python")
lp = float(lp)
lp = str(lp)
print ("lp is of type", type(lp))

