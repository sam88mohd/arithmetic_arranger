import operator

def arithmetic_arranger(problems, result=False):
  opts = {
      "+": operator.add,
      "-": operator.sub
  }

  top = []
  bottom = []
  lines = []
  results = []

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
    
    arranged_problems = "\n".join(["    ".join(chunk) for chunk in (top, bottom, lines)])
    
    if result:
      r = opts[chunks[1]](int(chunks[0]), int(chunks[2]))
      results.append(r)

      arranged_problems += "\n" + "    ".join([" ".join(str(result)) for result in results])
  return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

