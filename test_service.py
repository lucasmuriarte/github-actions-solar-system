"""
Simple probe that calls an HTTP service container.

It expects the service to expose `http://localhost:8080/status/200`
and return HTTP 200.  If the runner can start the service container
and reach that endpoint, the assertion passes.
"""
import requests

def test_service_container_reachable():
    url = "http://localhost:8080/status/200"
    r = requests.get(url, timeout=5)
    assert r.status_code == 200
    print("✓ service container reachable:", r.text[:40])
