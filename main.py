import string, random
from PIL import Image
choice = input("   1. ManyCensor   2. AnyWiggle\n   3. L33T5P34K    4. Img2ASCII\n   5. HELP (USE \"HELP\")\n(USE NUMBER) Choice: ")
if choice == "HELP":
  helper = input("What command do you need help with? (USE NUMBER) : ")
  if helper == "1":
   print("generate text like \"||t||||h||||i||||s||\". For formatting issues you must type \">:<\" at the begining and end.")
  elif helper == "2":
    print("Generate a wiggle copypasta using any phrase.")
  elif helper == "3":
    print("G3N3R4T3 T3XT L1K3 TH15.")
  elif helper == "4":
    print("Convert an image (path) to ASCII.")
elif choice == "1":
 orig = input("(begin text with \">:<\" and do NOT add a space after.)\nTEXT: ")
 spacefix_orig = orig.replace(" ", "<:>")
 spaced_spacefix = spacefix_orig.replace("", "||||")
 final = spaced_spacefix.replace("||<||||:||||>||", "||  ||")
 ffinal = final.replace("||||>||||:||||<||", "")
 print(ffinal)
elif choice == "2":
  wiggle = input("Wiggle: ")
  print(f"""
{wiggle}\n  {wiggle}\n    {wiggle}\n        {wiggle}\n          {wiggle}\n            {wiggle}\n              {wiggle}\n                {wiggle}\n                  {wiggle}\n                    {wiggle}\n                      {wiggle}\n                        {wiggle}\n                         {wiggle}\n                           {wiggle}\n                             {wiggle}\n                           {wiggle}\n                         {wiggle}\n                        {wiggle}\n                      {wiggle}\n                    {wiggle}\n                  {wiggle}\n                {wiggle}\n              {wiggle}\n            {wiggle}\n          {wiggle}\n        {wiggle}\n      {wiggle}\n    {wiggle}\n  {wiggle}\n{wiggle}""")
elif choice == "3":
  normal=input("Translate text : ") 
  replacements=(('e','3'),('i','1'),('o','0'),('a','4'),('s','5'))
  new_string = normal
  for old, new in replacements:
    new_string = new_string.replace(old, new)
  print(new_string.upper())
elif choice == "4":
  img = Image.open(input(".img path: "))
  width, height = img.size
  aspect_ratio = height/width
  new_width = 40
  new_height = aspect_ratio * new_width * 0.55
  img = img.resize((new_width, int(new_height)))
  img = img.convert('L')
  pixels = img.getdata()
  chars = ["B","S","#","&","@","$","%","*","!",":","."]
  new_pixels = [chars[pixel//25] for pixel in pixels]
  new_pixels = ''.join(new_pixels)
  new_pixels_count = len(new_pixels)
  ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
  ascii_image = "\n".join(ascii_image)
  print(ascii_image)
