import string
import random
from time import time
from unittest.mock import patch
from fastapi.testclient import TestClient

from app.main import app


@patch('app.settings.config.redis_db', 1)
def test_main():
    def get_random_link() -> str:
        return ''.join([random.choice(string.ascii_letters) for _ in range(random.randint(1, 20))]) + '.test'
    path = '/visited_links'
    link1 = get_random_link()
    link2 = get_random_link()
    data = {'links': [link1, link2]}
    bad_data = {'urls': [1, 2, 'test']}

    with TestClient(app) as client:
        response = client.post(path, json=data)
        bad_response = client.post(path, json=bad_data)
        empty_data_response = client.post(path, json={})

    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}
    assert bad_response.status_code == 422
    assert empty_data_response.status_code == 422

    path = '/visited_domains'
    query = '?from={}&to={}'
    from_, to_ = 0, int(time()) + 1
    with TestClient(app) as client:
        response = client.get(path + query.format(from_, to_))
        empty_response = client.get(path + query.format(0, 1))
        error_response = client.get(path)

    assert response.status_code == 200
    resp_data = response.json()
    assert 'status' in resp_data
    assert 'domains' in resp_data
    assert len(resp_data['domains']) > 0
    assert link1 in resp_data['domains']
    assert link2 in resp_data['domains']
    resp_data = empty_response.json()
    assert 'domains' in resp_data
    assert len(resp_data['domains']) == 0
    assert error_response.status_code == 422


