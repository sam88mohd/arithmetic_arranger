import operator

def arithmetic_arranger(problems, result=False):
  opts = {
      "+": operator.add,
      "-": operator.sub
  }

  for problem in problems:
    chunks = problem.split()
    print(chunks)

    
