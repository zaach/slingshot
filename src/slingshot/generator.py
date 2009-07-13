#!/usr/bin/env python
import optparse
import sys
import os
import shutil
import json

from os.path import join

import jsontemplate

slingshothomedir = join(os.path.expanduser('~'), '.slingshot')

def _readfile(filename):
  f = open(filename, "r")
  s = f.read()
  f.close()
  return s

class Generator:
  """Generator class
  """

  def __init__(self, template_dir):
    """
    Args:
      template_dir: The base directory of the template files
    """
    self.template_dir = template_dir
    self.project_dir = os.path.abspath(os.curdir)
    self.templates = []

  def _run(self, options):
    """Compile templates and run extra code
    Args:
      options: The JSON data
    """

    for root, dirs, files in os.walk(self.template_dir):
      for name in files:
        newfilename = jsontemplate.expand(name, options)
        oldpath = join(root, name)
        newpath = jsontemplate.expand(join(self.project_dir, oldpath.replace(self.template_dir+os.path.sep, '')), options)
        if os.path.exists(newpath) == False:
          try:
            oldfile = open(oldpath, "r")
            expanded = jsontemplate.FromFile(oldfile).expand(options, undefined_str='')
            oldfile.close()
            newfile = open(newpath, "w")
            newfile.write(expanded)
            newfile.close()
          except:
            print "Failed to compile file: "+oldpath
          print "\tcreate: "+newpath
        else:
          print "\texists: "+newpath

      for name in dirs:
        oldpath = join(root, name)
        newpath = jsontemplate.expand(join(self.project_dir, oldpath.replace(self.template_dir+os.path.sep, '')), options)

        if os.path.exists(newpath) == False:
          os.mkdir(newpath)
          print "\tcreate: "+newpath
        else:
          print "\texists: "+newpath

    print 'Done.'

  def run(self, options):
    self._run(options)

def loaddefaults(startpath=slingshothomedir):
  """Loads default JSON data found in home slinghot directory,
  or another if specified.
  """

  defaultjson = os.path.join(startpath, 'defaults.json')

  if os.path.exists(defaultjson):
    data = json.loads(_readfile(defaultjson))
  else:
    data = {}

  return data

def generate(filename, options={}):
  profiletmpl = join(slingshothomedir, 'generators', filename)
  slingshottmpl = os.path.abspath(join(os.path.dirname(os.path.realpath(__file__)), '..', 'generators', filename))

  if os.path.exists(profiletmpl):
    file = profiletmpl
  else:
    file = slingshottmpl

  if not os.path.exists(file):
    print "No such generator found"
    exit(1)

  data = loaddefaults()
  tmpldefaults = loaddefaults(file)
  data.update(tmpldefaults)
  data.update(options)

  gen = Generator(join(file, 'templates'))
  gen.run(data)

def main():
  usage = "usage: %prog [options] TEMPLATE"
  #TODO print available generators when no args

  p = optparse.OptionParser(usage=usage)
  p.add_option('--data', '-d', default="{}")

  options, arguments = p.parse_args()

  data = json.loads(options.data)

  try:
    param = arguments[0]
  except:
    return p.print_help()

  generate(param, data)

if __name__ == '__main__':
  main()
