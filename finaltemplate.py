import os

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname (_file_), 'templates')
jinja_env = jinja2.Environment (loader = jinja2.FileSystemLoader (template_dir), 
								autoescape = True)

class Handler(webapp2.RequestHandler):
	def write (self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str (self, template, **params):
		t = jinja_env.get_template(template)
		return t.render (params)
	
	def render (self, template, **kw):
    	self.write(self.render_str(template, **kw))
    
class MainPage(Handler):
    def get(self):
		items = self.request.get_all("colors")
        self.render("colors_list.html", items = items)
        
class FizzBuzzHandler(Handler):
	def post(self):
		n = self.request.get( 'n', o)
		n = n and int(n)
		self.render ('fizzbuzz.html', n = n)
		
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/fizzbuzz', FizzBuzzHandler),],
     debug=True)