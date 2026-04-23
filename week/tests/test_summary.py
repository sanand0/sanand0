import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import summary


def make_gemini_config() -> dict:
    return {
        "podcast_style": "Podcast style: Warm and lively.",
        "gemini": {
            "model": "gemini-3.1-flash-tts-preview",
            "ffmpeg_command": ["ffmpeg", "-i", "{pcm}", "{output}"],
            "speakers": [
                {
                    "name": "Alex",
                    "voice_name": "Algieba",
                    "profile": "Energetic, curious, and upbeat.",
                },
                {
                    "name": "Maya",
                    "voice_name": "Kore",
                    "profile": "Warm, clear, and grounded.",
                },
            ],
        },
    }


def test_build_gemini_request_uses_new_model_and_single_speaker_payload():
    config = make_gemini_config()

    segments, normalized_script, speakers = summary.split_script_segments(
        "Alex: [excited] Welcome back!\nMaya: Good to be here.\nAnd we have updates.",
        config,
    )

    assert normalized_script == (
        "Alex: [excited] Welcome back!\nMaya: Good to be here. And we have updates."
    )
    assert [speaker.name for speaker in speakers] == ["Alex", "Maya"]

    payload = summary.build_gemini_request(segments[0][1], segments[0][0], config)

    assert payload["model"] == "gemini-3.1-flash-tts-preview"
    assert payload["generationConfig"]["speechConfig"]["voiceConfig"] == {
        "prebuiltVoiceConfig": {"voiceName": "Algieba"}
    }
    assert "TRANSCRIPT" in payload["contents"][0]["parts"][0]["text"]


def test_main_tts_script_dry_run_validates_script_and_derives_output(
    tmp_path: Path, monkeypatch, capsys
):
    script_path = tmp_path / "sample-dialogue.md"
    script_path.write_text(
        "Alex: [excited] Welcome back.\nMaya: [laughs] We have two quick stories today.\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(summary, "load_config", lambda _script_dir: make_gemini_config())

    assert (
        summary.main(
            ["tts-script", "--script-file", str(script_path), "--dry-run"],
            script_dir=tmp_path,
        )
        == 0
    )

    result = json.loads(capsys.readouterr().out)
    assert result["command"] == "tts-script"
    assert result["status"] == "dry-run"
    assert result["speaker_names"] == ["Alex", "Maya"]
    assert result["audio_path"].endswith("sample-dialogue.mp3")


def test_main_describe_returns_machine_readable_schema(tmp_path: Path, capsys):
    assert summary.main(["--describe"], script_dir=tmp_path) == 0
    result = json.loads(capsys.readouterr().out)
    assert sorted(result["commands"]) == ["tts-script", "weekly"]


def test_build_week_paths_matches_expected_layout(tmp_path: Path):
    paths = summary.build_week_paths(tmp_path, "octocat", "2026-04-19")

    assert paths.week == "2026-04-19"
    assert paths.week_dir == tmp_path / "octocat-2026-04-19"
    assert paths.summary == paths.week_dir / "README.md"
    assert paths.context == paths.week_dir / "context.json"
    assert paths.podcast_script == paths.week_dir / "podcast-2026-04-19.md"
    assert paths.code_review == paths.week_dir / "code-review.md"
    assert paths.audio == paths.week_dir / "podcast-2026-04-19.mp3"
