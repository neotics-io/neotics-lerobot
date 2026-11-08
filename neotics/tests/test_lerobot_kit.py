import sys
from pathlib import Path

import pytest
from lerobot.datasets.lerobot_dataset import LeRobotDataset

KIT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT))

from episode_to_dataset import TASK, convert  # noqa: E402
from neotics_scene import load_episode  # noqa: E402


def test_dataset_reopens_with_the_same_numbers(tmp_path):
    episode = load_episode(KIT / "samples" / "depot.episode.json")
    root = tmp_path / "depot"
    convert(episode, str(root))

    reopened = LeRobotDataset("neotics/depot", root=str(root))
    assert len(reopened) == len(episode["time"]) and reopened.fps == episode["rate_hz"]
    assert reopened.meta.total_episodes == 1
    assert reopened.features["observation.state"]["names"] == episode["joints"]
    for frame in (0, 60, 125, 249):
        sample = reopened[frame]
        assert sample["observation.state"].tolist() == pytest.approx(episode["qpos"][frame], abs=1e-4)
        assert sample["action"].tolist() == pytest.approx(episode["ctrl"][frame], abs=1e-4)
        assert sample["task"] == TASK
