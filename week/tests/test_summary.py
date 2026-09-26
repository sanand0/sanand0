import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import summary


def test_format_and_parse_dialogue_preserve_style():
    turns = [
        {"speaker": "Alex", "text": "Hello.", "style": ""},
        {"speaker": "Maya", "text": "Important.", "style": "speaking slowly"},
    ]
    script = summary.format_dialogue(turns)

    assert script == "Alex: Hello.\nMaya: [style: speaking slowly] Important.\n"
    assert summary.parse_dialogue(script, ["Alex", "Maya"]) == turns


def test_format_dialogue_adds_blank_line_at_section_boundary():
    turns = [
        {"speaker": "Alex", "text": "First.", "style": "", "new_section": False},
        {"speaker": "Maya", "text": "New topic.", "style": "", "new_section": True},
    ]
    assert summary.format_dialogue(turns) == "Alex: First.\n\nMaya: New topic.\n"


def test_get_podcast_script_uses_luna_and_repository_context(monkeypatch, tmp_path):
    captured = {}

    class FakeResponse:
        output_text = json.dumps(
            {
                "turns": [
                    {"speaker": "Alex", "text": "Hello.", "style": ""},
                    {"speaker": "Maya", "text": "Hi.", "style": ""},
                ]
            }
        )

    class FakeResponses:
        def create(self, **kwargs):
            captured.update(kwargs)
            return FakeResponse()

    class FakeOpenAI:
        def __init__(self, **kwargs):
            self.responses = FakeResponses()

    monkeypatch.setattr(summary, "OpenAI", FakeOpenAI)
    monkeypatch.setattr(summary, "api_key", lambda *_: "test-key")
    monkeypatch.setattr(summary, "podcast_cache_dir", lambda: tmp_path)

    activity = [
        {"repo.name": "sanand0/tool", "message": "Improve caching", "files": []}
    ]
    context = {"sanand0/tool": {"description": "A useful tool"}}
    config = {
        "podcast": "Week $WEEK for $NAME. Target $TARGET_WORDS words.",
        "openai": {"model": "gpt-6-luna"},
    }

    script = summary.get_podcast_script(activity, context, config, "Anand", "2026-09-20")

    assert script == "Alex: Hello.\nMaya: Hi.\n"
    assert captured["model"] == "gpt-6-luna"
    assert "reasoning" not in captured
    source = captured["input"][1]["content"]
    assert "repository_context" in source
    assert "Improve caching" in source


def test_build_speech_content_adds_style_only_when_present():
    content = summary.build_speech_content(
        [
            {"speaker": "Alex", "text": "One", "style": ""},
            {"speaker": "Maya", "text": "Two", "style": "warmly"},
        ]
    )
    assert content[0]["annotations"][0] == {
        "type": "speech_metadata",
        "speaker": "Alex",
    }
    assert content[1]["annotations"][0]["style"] == "warmly"


def test_audio_plan_uses_configurable_model_and_chunks():
    config = {
        "gemini": {
            "model": "gemini-3.8-flash-lite-tts",
            "chunk_size": 2,
            "sample_rate": 24000,
            "speakers": [
                {"name": "Alex", "voice_name": "Algieba"},
                {"name": "Maya", "voice_name": "Kore"},
            ],
        }
    }
    script = "\n".join(
        [
            "Alex: One.",
            "Maya: Two.",
            "Alex: Three.",
            "Maya: Four.",
            "Alex: Five.",
        ]
    )

    plan = summary.audio_plan(script, config)

    assert plan["model"] == "gemini-3.8-flash-lite-tts"
    assert plan["turn_count"] == 5
    assert plan["chunk_count"] == 3
    assert plan["speaker_names"] == ["Alex", "Maya"]
