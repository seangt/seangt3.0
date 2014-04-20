import os
import logging
import wsgiref.handlers
from google.appengine.ext import webapp
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.ext import db


def doRender(handler, tname='main.htm', values={}):
    temp = os.path.join(
        os.path.dirname(__file__),
        'templates/' + tname)
    if not os.path.isfile(temp):
        return False
    
    # Check to see if we are supposed to be rendering 
    # A non-html file
    binary = False
    if temp.endswith(".jpg") or temp.endswith(".jpeg") :
        handler.response.headers['Content-Type'] = 'image/jpeg'
        binary = True
    elif temp.endswith(".png") :
        handler.response.headers['Content-Type'] = 'image/png'
        binary = True

    if binary:
        outstr = open(temp, "rb").read()
        handler.response.out.write(outstr)
        return True
    
    newval = dict(values)
    newval['path'] = handler.request.path
    
    outstr = template.render(temp, newval)
    handler.response.out.write(outstr)
    return True

class MainHandler(webapp2.RequestHandler):

  def get(self):

    if doRender(self,self.request.path) :
        return
    doRender(self,'main.htm')

app = webapp2.WSGIApplication([
    ('/.*', MainHandler)],
    debug=True)



