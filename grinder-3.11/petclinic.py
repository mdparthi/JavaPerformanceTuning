# The Grinder 3.11
# HTTP script recorded by TCPProxy at May 30, 2018 12:00:57 PM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

def createRequest(test, url, headers=None):
    """Create an instrumented HTTPRequest."""
    request = HTTPRequest(url=url)
    if headers: request.headers=headers
    test.record(request, HTTPRequest.getHttpMethodFilter())
    return request

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

connectionDefaults.defaultHeaders = \
  [ NVPair('Accept-Language', 'en-US,en;q=0.5'),
    NVPair('Accept-Encoding', 'gzip, deflate'),
    NVPair('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0'), ]

headers0= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ]

headers1= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://localhost:8080/'), ]

headers2= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8080/'), ]

headers3= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8080/resources/css/petclinic.css'), ]

headers4= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8080/'), ]

headers5= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8080/owners/find'), ]

headers6= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8080/owners/new'), ]

headers7= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8080/owners/12/edit'), ]

url0 = 'http://ocsp.digicert.com:80'
url1 = 'http://localhost:8080'

request101 = createRequest(Test(101, 'POST /'), url0, headers0)

# home
request201 = createRequest(Test(201, 'GET /'), url1, headers0)

request202 = createRequest(Test(202, 'GET petclinic.css'), url1)

request203 = createRequest(Test(203, 'GET favicon.png'), url1, headers0)

request204 = createRequest(Test(204, 'GET jquery-ui.min.js'), url1, headers1)

request205 = createRequest(Test(205, 'GET jquery.min.js'), url1, headers1)

request206 = createRequest(Test(206, 'GET pets.png'), url1, headers2)

request207 = createRequest(Test(207, 'GET spring-logo-dataflow.png'), url1)

request208 = createRequest(Test(208, 'GET bootstrap.min.js'), url1, headers1)

request209 = createRequest(Test(209, 'GET spring-pivotal-logo.png'), url1, headers2)

request301 = createRequest(Test(301, 'GET glyphicons-halflings-regular.woff'), url1, headers3)

request401 = createRequest(Test(401, 'GET montserrat-webfont.woff'), url1, headers3)

request501 = createRequest(Test(501, 'GET varela_round-webfont.woff'), url1, headers3)

request601 = createRequest(Test(601, 'GET /'), url1, headers4)

# find owner
request701 = createRequest(Test(701, 'GET find'), url1, headers4)

request801 = createRequest(Test(801, 'GET owners'), url1, headers5)

# veter
request901 = createRequest(Test(901, 'GET vets.html'), url1)

request1001 = createRequest(Test(1001, 'GET find'), url1)

# find
request1101 = createRequest(Test(1101, 'GET owners'), url1, headers5)

# add owner
request1201 = createRequest(Test(1201, 'GET new'), url1)

request1301 = createRequest(Test(1301, 'POST new'), url1, headers6)

request1401 = createRequest(Test(1401, 'POST new'), url1, headers6)

request1402 = createRequest(Test(1402, 'GET 12'), url1, headers6)

# edit
request1501 = createRequest(Test(1501, 'GET edit'), url1)

request1601 = createRequest(Test(1601, 'POST edit'), url1, headers7)

request1602 = createRequest(Test(1602, 'GET 12'), url1, headers7)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """POST / (request 101)."""
    result = request101.POST('/',
      "\x30\x51\x30\x4F\x30\x4D\x30\x4B\x30\x49\x30\x09\x06\x05\x2B\x0E"
      "\x03\x02\x1A\x05\x00\x04\x14\x10\x5F\xA6\x7A\x80\x08\x9D\xB5\x27"
      "\x9F\x35\xCE\x83\x0B\x43\x88\x9E\xA3\xC7\x0D\x04\x14\x0F\x80\x61"
      "\x1C\x82\x31\x61\xD5\x2F\x28\xE7\x8D\x46\x38\xB4\x2C\xE1\xC6\xD9"
      "\xE2\x02\x10\x0E\x87\xC3\xCD\x55\xD5\x7A\xE9\x73\xD2\x95\x2C\x19"
      "\x9D\xD8\xBF",
      ( NVPair('Content-Type', 'application/ocsp-request'), ))

    return result

  def page2(self):
    """GET / (requests 201-209)."""
    result = request201.GET('/')

    grinder.sleep(17)
    request202.GET('/resources/css/petclinic.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://localhost:8080/'), ))

    request203.GET('/resources/images/favicon.png')

    request204.GET('/webjars/jquery-ui/1.11.4/jquery-ui.min.js')

    request205.GET('/webjars/jquery/2.2.4/jquery.min.js')

    request206.GET('/resources/images/pets.png')

    request207.GET('/resources/images/spring-logo-dataflow.png', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://localhost:8080/resources/css/petclinic.css'), ))

    request208.GET('/webjars/bootstrap/3.3.6/js/bootstrap.min.js')

    request209.GET('/resources/images/spring-pivotal-logo.png')

    return result

  def page3(self):
    """GET glyphicons-halflings-regular.woff (request 301)."""
    result = request301.GET('/webjars/bootstrap/fonts/glyphicons-halflings-regular.woff')

    return result

  def page4(self):
    """GET montserrat-webfont.woff (request 401)."""
    result = request401.GET('/resources/fonts/montserrat-webfont.woff')

    return result

  def page5(self):
    """GET varela_round-webfont.woff (request 501)."""
    result = request501.GET('/resources/fonts/varela_round-webfont.woff')

    return result

  def page6(self):
    """GET / (request 601)."""
    result = request601.GET('/')

    return result

  def page7(self):
    """GET find (request 701)."""
    result = request701.GET('/owners/find')

    return result

  def page8(self):
    """GET owners (request 801)."""
    self.token_lastName = \
      'g'
    result = request801.GET('/owners' +
      '?lastName=' +
      self.token_lastName)

    return result

  def page9(self):
    """GET vets.html (request 901)."""
    result = request901.GET('/vets.html', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://localhost:8080/owners?lastName=g'), ))

    return result

  def page10(self):
    """GET find (request 1001)."""
    result = request1001.GET('/owners/find', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://localhost:8080/vets.html'), ))

    return result

  def page11(self):
    """GET owners (request 1101)."""
    self.token_lastName = \
      'James'
    result = request1101.GET('/owners' +
      '?lastName=' +
      self.token_lastName)

    return result

  def page12(self):
    """GET new (request 1201)."""
    result = request1201.GET('/owners/new', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://localhost:8080/owners?lastName=James'), ))

    return result

  def page13(self):
    """POST new (request 1301)."""
    result = request1301.POST('/owners/new',
      ( NVPair('firstName', 'test'),
        NVPair('lastName', 'test'),
        NVPair('address', 'st'),
        NVPair('city', 'sts'),
        NVPair('telephone', 'stststs'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page14(self):
    """POST new (requests 1401-1402)."""
    
    # Expecting 302 ''
    result = request1401.POST('/owners/new',
      ( NVPair('firstName', 'test'),
        NVPair('lastName', 'test'),
        NVPair('address', 'st'),
        NVPair('city', 'sts'),
        NVPair('telephone', '1231232222'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    request1402.GET('/owners/12')

    return result

  def page15(self):
    """GET edit (request 1501)."""
    result = request1501.GET('/owners/12/edit', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://localhost:8080/owners/12'), ))

    return result

  def page16(self):
    """POST edit (requests 1601-1602)."""
    
    # Expecting 302 ''
    result = request1601.POST('/owners/12/edit',
      ( NVPair('firstName', 'test'),
        NVPair('lastName', 'test'),
        NVPair('address', 'stersd'),
        NVPair('city', 'sts'),
        NVPair('telephone', '1231232222'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    request1602.GET('/owners/12')

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # POST / (request 101)

    grinder.sleep(20575)
    self.page2()      # GET / (requests 201-209)
    self.page3()      # GET glyphicons-halflings-regular.woff (request 301)
    self.page4()      # GET montserrat-webfont.woff (request 401)
    self.page5()      # GET varela_round-webfont.woff (request 501)

    grinder.sleep(1325)
    self.page6()      # GET / (request 601)

    grinder.sleep(8286)
    self.page7()      # GET find (request 701)

    grinder.sleep(4677)
    self.page8()      # GET owners (request 801)

    grinder.sleep(6470)
    self.page9()      # GET vets.html (request 901)

    grinder.sleep(2588)
    self.page10()     # GET find (request 1001)

    grinder.sleep(9512)
    self.page11()     # GET owners (request 1101)

    grinder.sleep(9483)
    self.page12()     # GET new (request 1201)

    grinder.sleep(8649)
    self.page13()     # POST new (request 1301)

    grinder.sleep(4200)
    self.page14()     # POST new (requests 1401-1402)

    grinder.sleep(6076)
    self.page15()     # GET edit (request 1501)

    grinder.sleep(2276)
    self.page16()     # POST edit (requests 1601-1602)


# Instrument page methods.
Test(100, 'Page 1').record(TestRunner.page1)
Test(200, 'Page 2').record(TestRunner.page2)
Test(300, 'Page 3').record(TestRunner.page3)
Test(400, 'Page 4').record(TestRunner.page4)
Test(500, 'Page 5').record(TestRunner.page5)
Test(600, 'Page 6').record(TestRunner.page6)
Test(700, 'Page 7').record(TestRunner.page7)
Test(800, 'Page 8').record(TestRunner.page8)
Test(900, 'Page 9').record(TestRunner.page9)
Test(1000, 'Page 10').record(TestRunner.page10)
Test(1100, 'Page 11').record(TestRunner.page11)
Test(1200, 'Page 12').record(TestRunner.page12)
Test(1300, 'Page 13').record(TestRunner.page13)
Test(1400, 'Page 14').record(TestRunner.page14)
Test(1500, 'Page 15').record(TestRunner.page15)
Test(1600, 'Page 16').record(TestRunner.page16)
