const PORT = 8000
const server = require('http') .createServer((req, res) => {
  res.setHeader('Set-Cookie', `last_access=${Date.now()};`);
  res.writeHead(200, {"Content-Type": "text/plain"})
  if (req.method == 'GET') {
    const body = ['get', req.headers.cookie, req.url.split('?').at(1)]
    res.end(body.join('\n'))
  }
  if (req.method == 'POST') {
    const body = ['post', req.headers.cookie]
    req.on('data', chunk => body.push(chunk))
    req.on('end', ()  => res.end(body.join('\n')))
  }
})
server.listen(PORT)

