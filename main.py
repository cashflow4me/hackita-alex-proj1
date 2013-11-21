#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
#import webapp2
#
#class MainHandler(webapp2.RequestHandler):
#    def get(self):
#        self.response.write('Hello world!')
#
#app = webapp2.WSGIApplication([
#    ('/', MainHandler)
#], debug=True)


__author__ = 'cashflow4me'
from bottle import route, default_app, run, get, post, request

#print "hello world"


def f_helloworld():
    return "Hello World"


def f_helloyou(name):
    return "Hello " + name


def f_99bottles(bottles):
    output = ""
    for i in range(bottles, 1, -1):
        #print i
        output += (str(i) + " bottles of beer on the wall, " + str(
            i) + " bottles of beer.<BR>\n Take one down, pass it around,<BR>\n " + str(
            i - 1) + " bottles of beer on the wall...<BR>\n")
    output += (
        "1 bottle of beer.<BR>\n Take one down, pass it around, no more beer on the wall...<BR>\n GO and buy some more...")
    return output


def f_99beers(bottles):
    output = str(bottles) + " bottles of beer on the wall, " + str(
        bottles) + " bottles of beer.<BR>\n If one of those bottles should happen to fall, " + str(
        bottles - 1) + " bottles of beer on the wall...<BR>\n"
    if bottles == 0:
        return "No more beer on the wall...<BR>\n GO and buy some more..."
    else:
        return output + f_99beers(bottles - 1)


@route('/')
def index():
    return '''
        Hello from bottle! :-) <br>
        <a href="/hello/">Hello World</a><br>
        <a href="/hello/Alex">Hello by name</a><br>
        <a href="/bottles-loop/">bottles by loop form</a><br>
        <a href="/bottles-loop/3">bottles by loop (3)</a><br>
        <a href="/bottles-recursion/">bottles by recursion form</a><br>
        <a href="/bottles-recursion/2">bottles by recursion (2)</a><br>
        '''


@route('/hello')
@route('/hello/')
def helloworld():
    return "Hello World"


@route('/hello/<name>')
def hello(name):
    if name == "":
        return "Hello World"
    else:
        return "Hello %s" % str(name)


@route('/bottles-loop')
@route('/bottles-loop/')
def bottlesloop_form():
    return '''
        <form action="/bottles-loop" method="post">
            bottles #: <input name="n" type="number" />
            <input value="send" type="submit" />
        </form>
    '''


@route('/bottles-loop/<n:int>')
def bottlesloop(n):
    if n == 0:
        return "No bottles, go buy some."
    else:
        return f_99bottles(n)

@get('/bottles-loop/<n:int>')
def bottlesloop_get(n):
    return bottlesloop(n)

@post('/bottles-loop')
def bottlesloop_post():
    return bottlesloop(int(request.forms.get('n'))) + "<BR>" + bottlesloop_form()


@route('/bottles-recursion')
@route('/bottles-recursion/')
def bottlesrecursion_form():
    return '''
        <form action="/bottles-recursion" method="post">
            bottles #: <input name="n" type="number" />
            <input value="send" type="submit" />
        </form>
    '''


#@route('/bottles-recursion/<n:int>')
def bottlesrecursion(n):
    if n <= 0:
        return "No bottles, go buy some."
    else:
        return str(f_99beers(n))

@get('/bottles-recursion/<n:int>')
def bottlesrecursion_get(n):
    return bottlesrecursion(n)


@post('/bottles-recursion')
def bottlesrecursion_post():
    return bottlesrecursion(int(request.forms.get('n'))) + "<BR>" + bottlesrecursion_form()

app = default_app()
