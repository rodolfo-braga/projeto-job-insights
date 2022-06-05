from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dict_jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert 'titulo' not in dict_jobs[0]
    assert 'salario' not in dict_jobs[0]
    assert 'tipo' not in dict_jobs[0]
    assert 'title' in dict_jobs[0]
    assert 'salary' in dict_jobs[0]
    assert 'type' in dict_jobs[0]
