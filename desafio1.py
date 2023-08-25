while True:
  T = input()
  if len(T) <= 1:
    continue
  elif len(T) > 500:
    continue
  else:
    TLimpo = T.strip()
    if len(TLimpo) <= 140:
      print("TWEET")
    else:
      print("MUTE")