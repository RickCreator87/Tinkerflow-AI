Phase 3: Dead-simple dashboard (FastAPI + HTML)

No React. No drama. Just HTML + fetch.
`
/admin/dashboard

from fastapi.responses import HTMLResponse

@router.get("/admin/dashboard", response_class=HTMLResponse)
def dashboard():
    return """
    <html>
      <body>
        <h1>AI Gateway Usage</h1>
        <pre id="data">Loading...</pre>

        <script>
          fetch('/admin/metrics', {
            headers: { 'x-admin-key': 'super-secret-admin-key' }
          })
          .then(r => r.json())
          .then(d => {
            document.getElementById('data').innerText =
              JSON.stringify(d, null, 2);
          });
        </script>
      </body>
    </html>
    """
