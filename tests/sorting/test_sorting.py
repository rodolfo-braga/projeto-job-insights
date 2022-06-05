import pytest
from src.sorting import sort_by


jobs = [
    {'min_salary': '', 'max_salary': '2000', 'date_posted': '2022-06-01'},
    {'min_salary': '2000', 'max_salary': '', 'date_posted': '2022-06-02'},
    {'min_salary': '3000', 'max_salary': '3000', 'date_posted': ''},
]

jobs_sorted_by_min_salary = [
    {'min_salary': '2000', 'max_salary': '', 'date_posted': '2022-06-02'},
    {'min_salary': '3000', 'max_salary': '3000', 'date_posted': ''},
    {'min_salary': '', 'max_salary': '2000', 'date_posted': '2022-06-01'},
]

jobs_sorted_by_max_salary = [
    {'min_salary': '3000', 'max_salary': '3000', 'date_posted': ''},
    {'min_salary': '', 'max_salary': '2000', 'date_posted': '2022-06-01'},
    {'min_salary': '2000', 'max_salary': '', 'date_posted': '2022-06-02'},
]

jobs_sorted_by_date_posted = [
    {'min_salary': '2000', 'max_salary': '', 'date_posted': '2022-06-02'},
    {'min_salary': '', 'max_salary': '2000', 'date_posted': '2022-06-01'},
    {'min_salary': '3000', 'max_salary': '3000', 'date_posted': ''},
]


def test_sort_by_criteria():
    sort_by(jobs, 'min_salary')
    assert jobs == jobs_sorted_by_min_salary

    sort_by(jobs, 'max_salary')
    assert jobs == jobs_sorted_by_max_salary

    sort_by(jobs, 'date_posted')
    assert jobs == jobs_sorted_by_date_posted

    with pytest.raises(ValueError):
        sort_by(jobs, 'invalid_criteria')
