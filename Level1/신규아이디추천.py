def solution(new_id):
  val = ""
    
  new_id = new_id.lower()

  condition = ['-','_','.']
  for a in new_id:
      if a.islower() or a.isalnum() or a in condition:
        val = val + a

  new_id = val
      
  while ".." in new_id:
      new_id = new_id.replace("..",".")
      
  if new_id[0] == '.':
    if len(new_id) >= 2:
      new_id = new_id[1:]

  if new_id[-1] == '.':
    new_id = new_id[:-1]
      
  if new_id == "":
    new_id = "a"
      
  if len(new_id) >= 16:
    new_id = new_id[:15]
      
    if new_id[-1] == ".":
        new_id = new_id[:-1]


  last_wd = new_id[-1:]

  while len(new_id) < 3:
    new_id += last_wd
      

  return new_id
