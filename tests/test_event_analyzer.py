from app.services.event_analyzer import extract_event_themes

def test_extract_event_themes():
    description = "Artificial Intelligence in Healthcare"
    themes = extract_event_themes(description)

    assert isinstance(themes, list)
    assert len(themes) == 3