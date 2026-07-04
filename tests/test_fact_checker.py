from app.services.fact_checker import fact_check

def test_fact_check():
    result = fact_check("Artificial intelligence")

    assert isinstance(result, str)
    assert len(result) > 0