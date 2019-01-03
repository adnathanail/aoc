from aocd import get_data
inputstring = get_data(day=1, year=2015)
openparenthesis = inputstring.count("(")
closeparenthesis = inputstring.count(")")
print(openparenthesis - closeparenthesis)
