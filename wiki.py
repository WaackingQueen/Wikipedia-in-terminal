#!/usr/bin/python

import wikipedia
import sys, getopt

def main():
   #If there are no arguments 
   if len(sys.argv) == 1:
      print 'USAGE: ./wiki.py "Search term" [no. sentences]'
      return

   #Default # of sentences if the only argument is 'topic' 
   topic = sys.argv[1]
   sentences = 10

   if len(sys.argv) > 2:
      sentences = int(sys.argv[2])

   print wikipedia.summary(topic, sentences = sentences)
   a = wikipedia.page(topic)
   b = a.url
   print ('''
   For more information click: 
   ''') + b

if __name__ == "__main__":
   main()