import operator

def arithmetic_arranger(problems, result=False):
  opts = {
      "+": operator.add,
      "-": operator.sub
  }

  top = []
  bottom = []
  lines = []

  for problem in problems:
    chunks = problem.split()
    max_len = len(chunks)
    line_len = max_len + 2

    first_num = chunks[0].rjust(line_len)
    second_num = f"{chunks[1]}{' ' * (line_len - len(chunks[2]) - 1)}{chunks[2]}"
    line = "-" * line_len

    top.append(first_num)
    bottom.append(second_num)
    lines.append(line)

    
    
  print(top, bottom, lines)
