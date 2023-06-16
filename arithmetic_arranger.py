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

  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    chunks = problem.split()
    max_len = max([len(chunk) for chunk in chunks])
    line_len = max_len + 2

    if max_len > 4:
      return "Error: Numbers cannot be more than four digits."
    elif chunks[1] not in opts.keys():
      return "Error: Operator must be '+' or '-'."
    elif not all([chunk.isnumeric() for chunk in chunks[::2]]):
      return "Error: Numbers must only contain digits."

    first_num = chunks[0].rjust(line_len)
    second_num = f"{chunks[1]}{' ' * (line_len - len(chunks[2]) - 1)}{chunks[2]}"
    line = "-" * line_len

    top.append(first_num)
    bottom.append(second_num)
    lines.append(line)
    
    arranged_problems = "\n".join(["    ".join(chunk) for chunk in (top, bottom, lines)])
    
    if result:
      calc = opts[chunks[1]](int(chunks[0]), int(chunks[2]))
      results.append(f"{str(calc).rjust(line_len)}")

      arranged_problems += "\n" + "    ".join(results)
  return arranged_problems


