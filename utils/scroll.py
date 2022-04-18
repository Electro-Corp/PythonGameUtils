  def scroll(text):
    d = ""
    text = "[system] "+text
    for line in text:
      a = 0
      for c in line:
        d+=(line[a])
        print(d,end="\r")
        time.sleep(0.05)
        a+=1
      print(d,end="\r")
    print(d,end="\r")
    print("")
