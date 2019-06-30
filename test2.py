import wikipedia
import sys, getopt

def main(argv):
   topic = ''
   sntncs = ''
   try:
      opts, args = getopt.getopt(argv, "t:s:", ["topic=", "sntncs=", ""])
   except getopt.GetoptError:
      print 'Wrong format' 
      print 'test.py -t <topic> -s <# of sentences>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-t", "--topic"):
         topic[] = arg
      elif opt in ("-s", "--sentences"):
         sntncs = arg
   
   print wikipedia.summary(list1, sentences = sntncs)
   a = wikipedia.page(topic)
   b = a.url
   print ('''
   For more information click: 
   ''') + b

if __name__ == "__main__":
   main(sys.argv[1:])